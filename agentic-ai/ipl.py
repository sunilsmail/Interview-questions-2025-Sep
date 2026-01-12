# ipl_langgraph_agent.py

import pandas as pd
from typing import TypedDict, List

from langchain_core.documents import Document
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_ollama import ChatOllama

from langgraph.graph import StateGraph, END



# =========================
# 1. VECTOR STORE SETUP
# =========================
import os

DB_PATH = "data/IPL_data"

print("Initializing Embeddings...")
embeddings = OllamaEmbeddings(model="nomic-embed-text")

if os.path.exists(DB_PATH):
    print(f"Existing DB found at {DB_PATH}. Loading...")
    vector_db = FAISS.load_local(DB_PATH, embeddings, allow_dangerous_deserialization=True)
else:
    print("No local DB found. Loading and processing data...")
    
    # 1. Load Data
    print("Loading IPL data...")
    matches = pd.read_csv("matches.csv")
    deliveries = pd.read_csv("deliveries.csv")

    # Identify finals (last match of each season)
    matches['date'] = pd.to_datetime(matches['date'], errors='coerce')
    finals_ids = matches.sort_values(['season', 'date']).drop_duplicates('season', keep='last')['id'].tolist()

    print("Matches columns:", matches.columns.tolist())
    print("Deliveries columns:", deliveries.columns.tolist())

    # 2. Convert to Documents
    documents: List[Document] = []
    
    # Match docs
    for _, row in matches.iterrows():
        stage = "Final" if row['id'] in finals_ids else "League Match"
        date_str = row['date'].strftime('%Y-%m-%d') if pd.notnull(row['date']) else "Unknown Date"
        
        text = (
            f"{stage} Match {row['id']} in season {row['season']} played on {date_str} at {row['venue']}. "
            f"{row['team1']} vs {row['team2']}. "
            f"Toss won by {row['toss_winner']} who chose to {row['toss_decision']}. "
            f"Winner: {row['winner']}. "
            f"Player of the match: {row.get('player_of_match', 'unknown')}."
        )
        documents.append(Document(page_content=text, metadata={"match_id": int(row["id"]), "season": str(row["season"])}))

    # Ball docs
    for _, r in deliveries.sample(3000, random_state=42).iterrows():
        total_runs = r['batsman_runs'] + r['extra_runs']
        text = (
            f"Match {r['match_id']} over {r['over']}.{r['ball']}: "
            f"{r['batter']} faced {r['bowler']} and scored "
            f"{r['batsman_runs']} runs, total runs on ball {total_runs}."
        )
        documents.append(Document(page_content=text, metadata={"match_id": int(r["match_id"])}))
    print(f"Total documents created: {len(documents)}")
    
    # 3. Split
    splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=50)
    chunks = splitter.split_documents(documents)
    print(f"Chunks created: {len(chunks)}")
    
    # 4. Create & Save DB
    print("Creating vector DB...")
    vector_db = FAISS.from_documents(chunks, embeddings)
    vector_db.save_local(DB_PATH)
    print(f"Vector DB saved to {DB_PATH}")

retriever = vector_db.as_retriever(search_kwargs={"k": 5})
print("Vector DB ready")


# =========================
# 5. DEFINE AGENT STATE
# =========================
class AgentState(TypedDict):
    question: str
    chat_history: List[BaseMessage]
    context: str
    answer: str


# =========================
# 6. DEFINE LLM (Chat Model)
# =========================
llm = ChatOllama(
    model="phi3:mini",
    temperature=0,
)


# =========================
# 7. RETRIEVAL NODE
# =========================
def retrieve_context(state: AgentState):
    print(f"\n--- [LOG] Retrieving context for: {state['question']} ---")
    docs = retriever.invoke(state["question"])
    context = "\n".join(d.page_content for d in docs)
    print(f"--- [LOG] Retrieved {len(docs)} documents. Context length: {len(context)} ---")
    return {"context": context}


# =========================
# 8. ANSWER NODE
# =========================
prompt = ChatPromptTemplate.from_template(
    """
You are an IPL cricket assistant.

Use conversation history to resolve references like "they", "that team".
Answer ONLY using the IPL context below.
If the answer is not present, say "I don't know".

Conversation History:
{chat_history}

IPL Context:
{context}

User Question:
{question}

Answer:
"""
)


def generate_answer(state: AgentState):
    print("--- [LOG] Generating answer... ---")
    history_text = "\n".join(
        f"{m.type}: {m.content}" for m in state["chat_history"]
    )

    messages = prompt.format_messages(
        chat_history=history_text,
        context=state["context"],
        question=state["question"],
    )

    response = llm.invoke(messages)
    print("--- [LOG] Answer generated. ---")

    return {"answer": response.content}


# =========================
# 9. MEMORY UPDATE NODE
# =========================
def update_memory(state: AgentState):
    return {
        "chat_history": state["chat_history"]
        + [
            HumanMessage(content=state["question"]),
            AIMessage(content=state["answer"]),
        ]
    }


# =========================
# 10. BUILD LANGGRAPH
# =========================
graph = StateGraph(AgentState)

graph.add_node("retrieve", retrieve_context)
graph.add_node("answer", generate_answer)
graph.add_node("memory", update_memory)

graph.set_entry_point("retrieve")
graph.add_edge("retrieve", "answer")
graph.add_edge("answer", "memory")
graph.add_edge("memory", END)

agent = graph.compile()


# =========================
# 11. CHAT LOOP
# =========================
print("\nIPL LangGraph Chatbot Ready!")
print("Type 'exit' to quit\n")

state: AgentState = {
    "question": "",
    "chat_history": [],
    "context": "",
    "answer": "",
}


    
# =========================
# ANALYTICS (PANDAS) FUNCTION
# =========================
def analytics_answer(question: str):
    q = question.lower()

    # Example: Who won IPL 2016?
    if "ipl" in q and "win" in q:
        # extract year
        for year in range(2008, 2026):
            if str(year) in q:
                season_matches = matches[matches["season"].astype(str).str.contains(str(year))]

                if season_matches.empty:
                    return None

                final_match = season_matches.sort_values("date").iloc[-1]
                winner = final_match["winner"]

                return f"{winner} won the IPL {year}."

    return None



while True:
    user_q = input("You: ")
    if user_q.lower() == "exit":
        break

    # 🔹 Step 1: Try deterministic analytics first
    analytics_result = analytics_answer(user_q)
    if analytics_result:
        print("Bot:", analytics_result)
        continue

    # 🔹 Step 2: Fall back to LangGraph RAG agent
    state["question"] = user_q
    state = agent.invoke(state)

    print("Bot:", state["answer"])
