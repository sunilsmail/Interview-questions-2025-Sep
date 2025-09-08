Here’s Part 1: Core JavaScript Concepts

📘 JavaScript Interview Q&A (Part 1 – Core Concepts)
<details> <summary>1. Objects in JavaScript</summary>

Objects are collections of key–value pairs.

const obj = {
  name: "John",
  age: 30,
};

// Access
console.log(obj.name); // John
console.log(obj["age"]); // 30

// Add
obj.city = "NY";

// Delete
delete obj.age;


👉 Ways to create objects:

Object literal {}

new Object()

Object.create(proto)

Constructor functions

ES6 Classes

</details>
<details> <summary>2. Arrays in JavaScript</summary>

Arrays are ordered collections.

const arr = [1, 2, 3];
arr.push(4);   // [1,2,3,4]
arr.pop();     // [1,2,3]
arr.shift();   // [2,3]
arr.unshift(1);// [1,2,3]


👉 Iteration:

for (let i = 0; i < arr.length; i++) console.log(arr[i]);
for (let val of arr) console.log(val); // for-of
arr.forEach(x => console.log(x));

</details>
<details> <summary>3. Functions</summary>

Function Declaration – hoisted

function add(a, b) {
  return a + b;
}


Function Expression

const add = function(a, b) { return a + b; };


Arrow Function

const add = (a, b) => a + b;

</details>
<details> <summary>4. typeof Operator</summary>
typeof "hello"; // "string"
typeof 10;      // "number"
typeof null;    // "object" ❌ (quirk)
typeof [];      // "object"
typeof {};      // "object"
typeof (()=>{});// "function"

</details>
<details> <summary>5. Scope</summary>

Global Scope → available everywhere.

Function Scope → variables inside function not accessible outside.

Block Scope (let, const) → available only inside {}.

if (true) {
  var x = 10; // function/global scoped
  let y = 20; // block scoped
}
console.log(x); // 10
console.log(y); // ReferenceError

</details>
<details> <summary>6. Callback</summary>

A function passed as argument to another function.

function greet(name, callback) {
  console.log("Hello " + name);
  callback();
}

greet("John", () => console.log("Callback executed!"));

</details>
<details> <summary>7. Promises</summary>
const promise = new Promise((resolve, reject) => {
  setTimeout(() => resolve("Done!"), 1000);
});

promise.then(res => console.log(res)).catch(err => console.error(err));


👉 States: pending → fulfilled/rejected.

</details>
<details> <summary>8. Async/Await</summary>

Syntactic sugar over Promises.

async function fetchData() {
  try {
    const res = await fetch("https://jsonplaceholder.typicode.com/todos/1");
    const data = await res.json();
    console.log(data);
  } catch (err) {
    console.error(err);
  }
}
fetchData();

</details>
<details> <summary>9. Map, Filter, Reduce, forEach</summary>
const arr = [1, 2, 3, 4];

arr.map(x => x * 2);        // [2,4,6,8]
arr.filter(x => x % 2 === 0); // [2,4]
arr.reduce((a, b) => a + b, 0); // 10
arr.forEach(x => console.log(x)); // prints each

</details>
<details> <summary>10. Spread & Rest</summary>
// Spread
const arr = [1,2,3];
const arr2 = [...arr, 4]; // [1,2,3,4]

// Rest
function sum(...nums) {
  return nums.reduce((a,b) => a+b);
}
console.log(sum(1,2,3)); // 6

</details>
<details> <summary>11. Closure</summary>

A function that remembers variables from its lexical scope.

function outer() {
  let count = 0;
  return function inner() {
    count++;
    return count;
  };
}
const counter = outer();
console.log(counter()); // 1
console.log(counter()); // 2

</details>
<details> <summary>12. Hoisting</summary>
console.log(a); // undefined
var a = 10;

sayHi(); // "Hi"
function sayHi() { console.log("Hi"); }


👉 var is hoisted (initialized as undefined).
👉 Functions are hoisted with full definition.

</details>
<details> <summary>13. Temporal Dead Zone (TDZ)</summary>

Using let or const before declaration causes TDZ error.

console.log(x); // ReferenceError
let x = 5;

</details>
<details> <summary>14. Call, Apply, Bind</summary>
function greet(greeting) {
  console.log(greeting + " " + this.name);
}
const user = { name: "John" };

greet.call(user, "Hello");   // Hello John
greet.apply(user, ["Hi"]);   // Hi John
const bound = greet.bind(user, "Hey");
bound(); // Hey John

</details>
<details> <summary>15. This Keyword</summary>

In global scope → window (browser).

Inside object method → that object.

In arrow functions → lexical this.

const obj = {
  name: "Alice",
  normal: function() { console.log(this.name); },
  arrow: () => console.log(this.name),
};

obj.normal(); // Alice
obj.arrow();  // undefined (or window.name)

</details>
<details> <summary>16. Prototypes & Prototypal Inheritance</summary>
function Person(name) {
  this.name = name;
}
Person.prototype.sayHi = function() {
  console.log("Hi, I’m " + this.name);
};

const p = new Person("Bob");
p.sayHi(); // Hi, I’m Bob


👉 Objects inherit from other objects via prototype chain.

</details>

✅ That’s Part 1 (Core).
