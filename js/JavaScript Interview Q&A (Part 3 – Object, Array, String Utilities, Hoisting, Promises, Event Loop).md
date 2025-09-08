# 📘 JavaScript Interview Q&A (Part 3 – Object, Array, String Utilities, Hoisting, Promises, Event Loop)

---

## 26. How can we restrict an object from modification?
<details> <summary>👉 Answer</summary>

Use **`Object.freeze()`** to prevent modification.

```js
const obj = { name: "JS" };
Object.freeze(obj);

obj.name = "Changed";  // ❌ won't work
obj.newProp = "Hello"; // ❌ won't work

console.log(obj); // { name: "JS" }
```
</details>

## 27. How many ways can we create an object?
<details> <summary>👉 Answer</summary>
Object literal

```js
const obj = { a: 1 };
new Object()


const obj = new Object();
obj.a = 1;
Constructor function


function Person(name) {
  this.name = name;
}
const p = new Person("John");
Object.create()


const proto = { greet: () => console.log("Hi") };
const obj = Object.create(proto);
Class


class Car {
  constructor(model) {
    this.model = model;
  }
}
const c = new Car("BMW");
```
</details>

## 28. Object Comparison (Shallow)
<details> <summary>👉 Answer</summary>
```js
function isEqual(obj1, obj2) {
  return JSON.stringify(obj1) === JSON.stringify(obj2);
}

console.log(isEqual({ a: 1 }, { a: 1 })); // true
```
</details>

## 29. Remove Duplicates from Array
<details> <summary>👉 Answer</summary>
```js
let arr = [1,1,2,2,3,3];
let unique = [...new Set(arr)];

console.log(unique); // [1,2,3]
```
</details>

## 30. Count Duplicates in Array
<details> <summary>👉 Answer</summary>
```js
let arr = [1,2,2,3,3,3];
let count = {};

arr.forEach(num => count[num] = (count[num] || 0) + 1);

console.log(count); // {1:1, 2:2, 3:3}
```
</details>

## 31. Flatten Array
<details> <summary>👉 Answer</summary>
```js
let arr = [1,[2,[3,[4]]]];
console.log(arr.flat(Infinity)); // [1,2,3,4]
```
</details>

## 32. Array/Object Grouping
<details> <summary>👉 Answer</summary>
```js
let arr = [
  { dept: "IT", name: "A" },
  { dept: "HR", name: "B" },
  { dept: "IT", name: "C" }
];

let grouped = arr.reduce((acc, item) => {
  (acc[item.dept] = acc[item.dept] || []).push(item.name);
  return acc;
}, {});

console.log(grouped); 
// { IT: ["A", "C"], HR: ["B"] }
```
</details>

## 33. Check if String has Number
<details> <summary>👉 Answer</summary>
```js
let str = "Welcome123";
console.log(/\d/.test(str)); // true
```
</details>

## 34. Extract and Sum Numbers from String
<details> <summary>👉 Answer</summary>
```js
let str = "AB_12_cd_34_EF_87";
let sum = str.match(/\d+/g).reduce((a, b) => a + Number(b), 0);

console.log(sum); // 133
```
</details>

## 35. Expression Trick
<details> <summary>👉 Answer</summary>
```js
let x = 1;
x = (x++, 4);
console.log(x); // 4
```
</details>

## 36. Edge Cases
<details> <summary>👉 Answer</summary>
```js
console.log(!!0);                 // false
console.log(2 === "2");           // false
console.log({} === Object);       // false
console.log(3 ** 4);              // 81
console.log(parseInt(0.0000005)); // 5 (scientific notation issue)
```
</details>

## 37. Hoisting & Scope Example 1
<details> <summary>👉 Answer</summary>
```js
function fun() {
  setTimeout(() => {
    console.log(x); // undefined
    console.log(y); // ReferenceError
  });
  
  var x = 2;
  let y = 12;
}
fun();
```
</details>

## 38. Hoisting & Scope Example 2
<details> <summary>👉 Answer</summary>
```js
function fun(a, b){}
console.log(fun.length); // 2

var a = 15;
if (a) {
  let a = 4;
  const b = 5;
  var c = 6;
}

console.log(a); // 15
console.log(c); // 6
console.log(d); // ReferenceError
```
</details>

## 39. Promise.all
<details> <summary>👉 Answer</summary>
```js
let p1 = Promise.resolve(1);
let p2 = Promise.resolve(2);

Promise.all([p1, p2]).then(console.log); // [1, 2]
```
</details>

## 40. Promise.all with Async/Await
<details> <summary>👉 Answer</summary>
```js
async function run() {
  let results = await Promise.all([
    Promise.resolve("A"),
    Promise.resolve("B")
  ]);
  console.log(results); // ["A","B"]
}
run();
```
</details>

## 41. Promises with API
<details> <summary>👉 Answer</summary>
```js
fetch("https://jsonplaceholder.typicode.com/posts/1")
  .then(res => res.json())
  .then(data => console.log(data));
```
</details>

## 42. process.nextTick vs setImmediate
<details> <summary>👉 Answer</summary>
```js
console.log("Start");

setTimeout(() => console.log("setTimeout"), 0);

setImmediate(() => console.log("setImmediate"));

process.nextTick(() => console.log("nextTick"));

console.log("End");
Output Order:
Start
End
nextTick
setTimeout / setImmediate (depends on environment)
```
</details>
