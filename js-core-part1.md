# JavaScript Interview Q&A (Part 1 – Core Concepts)
## 1. Objects in JavaScript
<details> <summary>👉 Answer</summary>

Objects are collections of key–value pairs.

```js
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
```
</details>

## 2. Arrays in JavaScript
<details> <summary>👉 Answer</summary>

```js
const arr = [1, 2, 3];
arr.push(4);   // [1,2,3,4]
arr.pop();     // [1,2,3]
arr.shift();   // [2,3]
arr.unshift(1);// [1,2,3]

// Iteration
for (let i = 0; i < arr.length; i++) console.log(arr[i]);
for (let val of arr) console.log(val); // for-of
arr.forEach(x => console.log(x));
```

</details>

## 3. Functions
<details> <summary>👉 Answer</summary>

```js

Function Declaration – hoisted

function add(a, b) {
  return a + b;
}


Function Expression

const add = function(a, b) { return a + b; };


Arrow Function

const add = (a, b) => a + b;
```

</details>

## 4. typeof Operator
<details> <summary>👉 Answer</summary>

```js
typeof "hello"; // "string"
typeof 10;      // "number"
typeof null;    // "object" ❌ (quirk)
typeof [];      // "object"
typeof {};      // "object"
typeof (()=>{});// "function"
```

</details>

## 5. Scope
<details> <summary>👉 Answer</summary>

```js
if (true) {
  var x = 10; // function/global scoped
  let y = 20; // block scoped
}
console.log(x); // 10
console.log(y); // ReferenceError


👉 Types:

Global Scope

Function Scope

Block Scope (let, const)
```

</details>
## 6. Callback
<details> <summary>👉 Answer</summary>

```js

A function passed as argument to another function.

function greet(name, callback) {
  console.log("Hello " + name);
  callback();
}

greet("John", () => console.log("Callback executed!"));
```

</details>

## 7. Promises
<details> <summary>👉 Answer</summary>

```js
const promise = new Promise((resolve, reject) => {
  setTimeout(() => resolve("Done!"), 1000);
});

promise.then(res => console.log(res)).catch(err => console.error(err));


👉 States: pending → fulfilled/rejected
```

</details>

## 8. Async/Await
<details> <summary>👉 Answer</summary>

```js
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
```

</details>

## 9. Map, Filter, Reduce, forEach
<details> <summary>👉 Answer</summary>

```js
const arr = [1, 2, 3, 4];

arr.map(x => x * 2);        // [2,4,6,8]
arr.filter(x => x % 2 === 0); // [2,4]
arr.reduce((a, b) => a + b, 0); // 10
arr.forEach(x => console.log(x)); // prints each
```

</details>

## 10. Spread & Rest
<details> <summary>👉 Answer</summary>

```js
// Spread
const arr = [1,2,3];
const arr2 = [...arr, 4]; // [1,2,3,4]

// Rest
function sum(...nums) {
  return nums.reduce((a,b) => a+b);
}
console.log(sum(1,2,3)); // 6
```

</details>

## 11. Closure
<details> <summary>👉 Answer</summary>

```js

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
```

</details>

## 12. Hoisting
<details> <summary>👉 Answer</summary>

```js
console.log(a); // undefined
var a = 10;

sayHi(); // "Hi"
function sayHi() { console.log("Hi"); }


👉 var is hoisted (initialized as undefined).
👉 Functions are hoisted with full definition.
```

</details>

## 13. Temporal Dead Zone (TDZ)
<details> <summary>👉 Answer</summary>

```js
console.log(x); // ReferenceError
let x = 5;


👉 TDZ = using let/const before declaration.
```

</details>

## 14. Call, Apply, Bind
<details> <summary>👉 Answer</summary>

```js
function greet(greeting) {
  console.log(greeting + " " + this.name);
}
const user = { name: "John" };

greet.call(user, "Hello");   // Hello John
greet.apply(user, ["Hi"]);   // Hi John
const bound = greet.bind(user, "Hey");
bound(); // Hey John
```

</details>

## 15. This Keyword
<details> <summary>👉 Answer</summary>

```js
const obj = {
  name: "Alice",
  normal: function() { console.log(this.name); },
  arrow: () => console.log(this.name),
};

obj.normal(); // Alice
obj.arrow();  // undefined (or window.name)


👉 Rules:

Global → window (browser)

Inside object → that object

Arrow functions → lexical this
```

</details>

## 16. Prototypes & Prototypal Inheritance
<details> <summary>👉 Answer</summary>

```js
function Person(name) {
  this.name = name;
}
Person.prototype.sayHi = function() {
  console.log("Hi, I’m " + this.name);
};

const p = new Person("Bob");
p.sayHi(); // Hi, I’m Bob


👉 Objects inherit from other objects via prototype chain.

```

</details>
