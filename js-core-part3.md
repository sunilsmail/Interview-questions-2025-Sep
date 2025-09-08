JavaScript Interview Q&A – Part 3
🌀 Object Utilities
🔹 How can we restrict an object from modification?

👉 Use Object.freeze()

const obj = { name: "JS" };
Object.freeze(obj);

obj.name = "Changed"; // ❌ won't work
obj.newProp = "Hello"; // ❌ won't work
console.log(obj); // { name: "JS" }

🔹 How many ways can we create an object?

Object literal

const obj = { a: 1 };


new Object()

const obj = new Object();
obj.a = 1;


Constructor function

function Person(name) { this.name = name; }
const p = new Person("John");


Object.create()

const proto = { greet: () => console.log("Hi") };
const obj = Object.create(proto);


Class

class Car { constructor(model) { this.model = model; } }
const c = new Car("BMW");

🔹 Object comparison (shallow)
function isEqual(obj1, obj2) {
  return JSON.stringify(obj1) === JSON.stringify(obj2);
}
console.log(isEqual({ a: 1 }, { a: 1 })); // true

🌀 Array Utilities
🔹 Remove duplicates
let arr = [1,1,2,2,3,3];
let unique = [...new Set(arr)];
console.log(unique); // [1,2,3]

🔹 Count duplicates
let arr = [1,2,2,3,3,3];
let count = {};
arr.forEach(num => count[num] = (count[num] || 0) + 1);
console.log(count); // {1:1, 2:2, 3:3}

🔹 Flatten array
let arr = [1,[2,[3,[4]]]];
console.log(arr.flat(Infinity)); // [1,2,3,4]

🔹 Array/Object grouping
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

🌀 String / Number Utilities
🔹 Check whether string has number
let str = "Welcome123";
console.log(/\d/.test(str)); // true

🔹 Extract and sum numbers from string
let str = "AB_12_cd_34_EF_87";
let sum = str.match(/\d+/g).reduce((a, b) => a + Number(b), 0);
console.log(sum); // 133

🔹 Expression
let x = 1;
x = (x++, 4);
console.log(x); // 4

🔹 Edge cases
console.log(!!0); // false
console.log(2 === "2"); // false
console.log({} === Object); // false
console.log(3 ** 4); // 81
console.log(parseInt(0.0000005)); // 5 (scientific notation issue)

🌀 Hoisting & Scope Questions
🔹 Example 1
function fun(){
  setTimeout(()=>{
    console.log(x); // undefined
    console.log(y); // ReferenceError
  })
  var x = 2;
  let y = 12;
}
fun();

🔹 Example 2
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

🌀 Promises
🔹 promise.all
let p1 = Promise.resolve(1);
let p2 = Promise.resolve(2);
Promise.all([p1, p2]).then(console.log); // [1, 2]

🔹 promise.all with async/await
async function run() {
  let results = await Promise.all([
    Promise.resolve("A"),
    Promise.resolve("B")
  ]);
  console.log(results); // ["A","B"]
}
run();

🔹 Promises with API
fetch("https://jsonplaceholder.typicode.com/posts/1")
  .then(res => res.json())
  .then(data => console.log(data));

🌀 Event Loop
🔹 process.nextTick vs setImmediate
console.log("Start");

setTimeout(() => console.log("setTimeout"), 0);

setImmediate(() => console.log("setImmediate"));

process.nextTick(() => console.log("nextTick"));

console.log("End");


👉 Output order:

Start
End
nextTick
setTimeout / setImmediate (depends on environment)


✅ That’s Part 3.
