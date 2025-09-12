1. Object destruction with rename prop name
2. What is the OPTIONS in nodejs rest api
3. Different between rest vs graphql 
4. Write an sql query to fetch authors for a book and a book can have multiple authors 
5. What is the difference between using callback function as arrow function or normal function 
6. Difference between reducer and generator function

Answer for all the questions with md format 
ChatGPT said:

Here’s a clear breakdown of all your questions with answers in Markdown format:

1. Object Destructuring with Rename Property Name

You can rename a property while destructuring in JavaScript:

const user = { id: 1, username: "sunil", age: 30 };

// Destructure and rename `username` to `name`
const { username: name, age } = user;

console.log(name); // "sunil"
console.log(age);  // 30


👉 username: name means: take username from the object but store it in a variable called name.

2. What is the OPTIONS in Node.js REST API?

OPTIONS is an HTTP method mainly used in CORS (Cross-Origin Resource Sharing).

It asks the server: "What HTTP methods and headers are allowed for this resource?"

The server responds with headers like Access-Control-Allow-Methods and Access-Control-Allow-Headers.

Example in Express.js:

app.options("/api/data", (req, res) => {
  res.set("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE");
  res.set("Access-Control-Allow-Headers", "Content-Type, Authorization");
  res.sendStatus(200);
});

3. Difference Between REST vs GraphQL
Feature	REST	GraphQL
Data Fetching	Multiple endpoints, fixed responses	Single endpoint, client specifies data shape
Overfetching	Possible (extra fields you don’t need)	Avoided (fetch only requested fields)
Underfetching	Possible (need multiple calls for related data)	Avoided (can fetch related data in one query)
Versioning	Often requires versioned endpoints (/v1)	Not needed, schema evolves with deprecations
Performance	Multiple requests may be required	One request can return everything needed

👉 REST = resource-oriented, GraphQL = query-oriented.

4. SQL Query to Fetch Authors for a Book (Many-to-Many)

Suppose we have tables:

books(id, title)

authors(id, name)

book_authors(book_id, author_id)

Query:

SELECT b.title, a.name AS author
FROM books b
JOIN book_authors ba ON b.id = ba.book_id
JOIN authors a ON ba.author_id = a.id
WHERE b.title = 'The Great Book';


👉 This returns all authors for the book The Great Book.

5. Difference Between Callback Function as Arrow vs Normal Function
Arrow Function as Callback

Does not bind its own this (lexical this).

Useful when you want this to refer to the surrounding scope.

function Person() {
  this.age = 0;

  setInterval(() => {
    this.age++;  // `this` refers to Person instance
    console.log(this.age);
  }, 1000);
}
new Person();

Normal Function as Callback

Has its own this, depends on how it’s called.

In callbacks, often this becomes undefined or global.

function Person() {
  this.age = 0;

  setInterval(function () {
    this.age++;  // `this` is not Person (it’s global/undefined in strict mode)
    console.log(this.age);
  }, 1000);
}
new Person(); // NaN


👉 Use arrow functions in callbacks when you want to preserve lexical this.

6. Difference Between Reducer and Generator Function
Aspect	Reducer Function	Generator Function
Definition	Pure function (state, action) => newState	Function that can pause and resume (function*)
Use Case	State management (e.g., Redux)	Iteration, async flow control, producing sequences
Return Value	Returns new state once	Returns an iterator object with .next()
Execution	Runs fully when called	Executes lazily, step by step
Example	reduce() array method, Redux reducers	yield values one by one

Reducer Example:

function counterReducer(state, action) {
  switch (action.type) {
    case "increment": return state + 1;
    case "decrement": return state - 1;
    default: return state;
  }
}


Generator Example:

function* numberGen() {
  yield 1;
  yield 2;
  yield 3;
}
const gen = numberGen();
console.log(gen.next()); // { value: 1, done: false }


✅ Would you like me to also prepare short interview-style answers for each (like one-liners) so you can quickly revise before interviews?

You said:
const user = { id: 1, username: "sunil", age: 30 };

// Destructure and rename username to name
const { username: name, age } = user;

console.log(name); // "sunil"
console.log(age); 
 // 30

Nested object destruction 
ChatGPT said:

Good question 👍
Let’s extend this with nested object destructuring examples.

Example: Nested Object Destructuring
const user = {
  id: 1,
  username: "sunil",
  age: 30,
  address: {
    city: "Bangalore",
    country: "India",
    pin: 560001,
  },
  social: {
    github: "sunil-git",
    twitter: "sunil_twt",
  },
};

// Destructure nested objects
const {
  username: name,     // rename username → name
  address: { city, country },   // pick city & country from nested object
  social: { github: gitHandle } // rename github → gitHandle
} = user;

console.log(name);       // "sunil"
console.log(city);       // "Bangalore"
console.log(country);    // "India"
console.log(gitHandle);  // "sunil-git"

Example: With Default Values
const {
  address: { pin = "000000" }, // if pin missing, default will apply
  social: { linkedin = "N/A" } // property doesn’t exist → fallback
} = user;

console.log(pin);      // 560001
console.log(linkedin); // "N/A"

Example: Deeply Nested with Renaming
const company = {
  name: "TechCorp",
  location: {
    office: {
      city: "Hyderabad",
      floor: 5,
    }
  }
};

const {
  location: {
    office: { city: officeCity, floor }
  }
} = company;

console.log(officeCity); // "Hyderabad"
console.log(floor);      // 5


👉 Nested destructuring is super useful when handling APIs or config objects.

Do you want me to also show how to combine nested destructuring with arrays (like extracting authors from a book object with an array of authors)?