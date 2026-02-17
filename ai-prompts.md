Act as a Principal Software Architect and AI Systems Engineer.

Design and generate a COMPLETE production-ready AI-powered eCommerce Chatbot Platform with:

- Microservices architecture
- FastAPI backend services
- LangGraph / LangChain multi-agent orchestration
- PostgreSQL database
- Redis for memory
- React frontend (chat UI)
- Dockerized services
- Kubernetes deployment manifests
- Clean Architecture + SOLID principles
- Fully async implementation
- Production-level folder structure

====================================================
🎯 BUSINESS GOAL
====================================================

Build an AI chatbot system that supports:

1. Product-level policy queries
2. Cancel specific product in an order
3. Update delivery date
4. Track order
5. Refund eligibility
6. Maintain chat history
7. Multi-turn conversation memory
8. Escalation to human agent

====================================================
🏗 ARCHITECTURE REQUIREMENTS
====================================================

Use Microservices:

1. API Gateway
2. Auth Service
3. Order Service
4. Policy Service
5. Chat Service (AI Agent Orchestrator)
6. Notification Service (event-driven)

Services communicate via REST and internal service calls.

Add event-driven architecture using Redis Pub/Sub or Kafka (if possible).

====================================================
🧠 AI AGENT ARCHITECTURE (LangGraph)
====================================================

Implement Multi-Agent Workflow using LangGraph:

Agents:

1. Intent Classifier Agent
   - Detect intents:
     - track_order
     - cancel_product
     - update_delivery_date
     - product_policy_query
     - refund_status
     - escalate_to_human
   - Output structured JSON:
     {
       "intent": "",
       "confidence": 0.0,
       "entities": {}
     }

2. Order Agent
   - Calls Order Service
   - Validates order state

3. Policy Agent
   - Retrieves policy from DB
   - Validates cancellation window

4. Memory Agent
   - Uses Redis for session memory
   - Maintains conversation context

5. Orchestrator Node
   - Routes based on detected intent

Use GPT model with structured output parsing.

====================================================
⚙ BACKEND REQUIREMENTS (FastAPI)
====================================================

Use:

- FastAPI
- SQLAlchemy Async
- PostgreSQL
- Redis
- JWT Authentication
- Pydantic v2
- Structlog logging
- Dependency Injection pattern

Generate:

- Complete folder structure
- Models
- Schemas
- Repositories
- Service layer
- Routers
- Dependency wiring
- Middleware (logging, auth)
- Exception handling

====================================================
🗄 DATABASE DESIGN
====================================================

Tables:

Users
Orders
OrderItems
Products
Policies
ChatSessions
ChatMessages

Include:
- Proper foreign keys
- Indexes
- Status enums
- Migration-ready design

====================================================
🌐 API ENDPOINTS
====================================================

Auth:
POST /auth/register
POST /auth/login

Orders:
GET /orders/{order_id}
POST /orders/{order_id}/cancel
POST /orders/{order_id}/update-delivery
GET /orders/user/{user_id}

Policies:
GET /policies/product/{product_id}

Chat:
POST /chat/message
GET /chat/history/{session_id}

====================================================
💬 FRONTEND (React)
====================================================

Build:

- React + Vite
- Chat UI component
- Message bubbles
- Auto-scroll
- Loading state
- Session-based chat
- Auth token handling
- Axios service layer

Include:
- Folder structure
- API integration layer
- Reusable components

====================================================
🐳 DOCKER REQUIREMENTS
====================================================

Generate:

- Dockerfile for each service
- docker-compose.yml
- Environment variables
- Production-ready configuration

====================================================
☸ KUBERNETES REQUIREMENTS
====================================================

Generate:

- Deployment YAML for each service
- Service YAML
- Ingress configuration
- ConfigMap
- Secrets
- Horizontal Pod Autoscaler
- PostgreSQL + Redis manifests

====================================================
🔐 SECURITY
====================================================

- JWT-based authentication
- Role-based authorization
- Input validation
- Rate limiting
- CORS configuration

====================================================
📦 BONUS FEATURES
====================================================

- Add WebSocket support for real-time chat
- Add retry logic for LLM calls
- Add RAG support using PGVector
- Add CI/CD GitHub Actions example
- Add monitoring (Prometheus + Grafana)
- Add structured logging

====================================================
📄 DELIVERABLE FORMAT
====================================================

Provide:

1. Complete folder structure
2. All service code (not placeholders)
3. Sample .env file
4. Docker setup
5. Kubernetes manifests
6. Example API request/response
7. How to run locally
8. How to deploy to Kubernetes
9. Unit test examples using pytest
10. Clear explanations for each layer

Code must be:

- Fully async
- Production-grade
- Clean Architecture compliant
- Modular
- Scalable
- Enterprise-ready

Do not skip files.
Do not provide pseudo code.
Provide working code blocks.
