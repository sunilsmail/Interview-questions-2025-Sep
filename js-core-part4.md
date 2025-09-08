🌀 Event Propagation
❓ What are the phases of Event Propagation?

Capturing Phase – Event goes from root → target.

Target Phase – Event reaches the actual target element.

Bubbling Phase – Event bubbles from target → root.

❓ Example: Bubbling vs Capturing
<div id="parent">
  <button id="child">Click</button>
</div>

<script>
document.getElementById("parent").addEventListener("click", () => {
  console.log("Parent capturing");
}, true); // Capturing

document.getElementById("parent").addEventListener("click", () => {
  console.log("Parent bubbling");
}, false); // Bubbling

document.getElementById("child").addEventListener("click", () => {
  console.log("Child clicked");
});
</script>


👉 Click button:

Parent capturing
Child clicked
Parent bubbling

❓ stopPropagation vs preventDefault
document.getElementById("child").addEventListener("click", (e) => {
  e.stopPropagation(); // Stops bubbling
  e.preventDefault();  // Prevents default action (e.g. link navigation)
});

❓ Event Delegation Example
document.getElementById("parent").addEventListener("click", (e) => {
  if (e.target.tagName === "BUTTON") {
    console.log("Button clicked:", e.target.id);
  }
});

🌀 Currying
❓ What is Currying?

Transforming a function with multiple args into a sequence of functions with one arg each.

function sum(a) {
  return function(b) {
    return function(c) {
      return a + b + c;
    };
  };
}

console.log(sum(1)(2)(3)); // 6

🌀 Higher-Order Functions (HOFs)
❓ Definition

A function that takes another function as argument or returns a function.

function hof(fn) {
  return function(x) {
    return fn(x) * 2;
  };
}

const doubleSquare = hof((n) => n * n);
console.log(doubleSquare(3)); // 18

🌀 ES6 Features (Commonly Asked)

let and const

Arrow functions

Template literals

Default parameters

Destructuring

Spread/Rest operators

Classes

Modules (import/export)

Promises & async/await

Map, Set, WeakMap, WeakSet

Symbol

Generators

Optional chaining (?.)

Nullish coalescing (??)

🌀 Debugging Techniques

console.log for values.

console.table for arrays/objects.

console.time / console.timeEnd for performance.

debugger; keyword to pause execution in DevTools.

Chrome DevTools: Breakpoints, watch expressions.

Node.js Inspector: Run with node inspect.

🌀 Generators
❓ What is a Generator?

A special function that can pause and resume using yield.

function* gen() {
  yield 1;
  yield 2;
  yield 3;
}

const g = gen();
console.log(g.next().value); // 1
console.log(g.next().value); // 2
console.log(g.next().value); // 3

🌀 Shallow Copy vs Deep Copy
// Shallow Copy
let obj1 = { a: 1, b: { c: 2 } };
let shallow = { ...obj1 };
shallow.b.c = 5;
console.log(obj1.b.c); // 5 (reference shared)

// Deep Copy
let obj2 = { a: 1, b: { c: 2 } };
let deep = structuredClone(obj2);
deep.b.c = 10;
console.log(obj2.b.c); // 2

🌀 Polyfills
❓ Example: Polyfill for Array.map
Array.prototype.myMap = function(callback) {
  let result = [];
  for (let i = 0; i < this.length; i++) {
    result.push(callback(this[i], i, this));
  }
  return result;
};

console.log([1, 2, 3].myMap(x => x * 2)); // [2, 4, 6]

🌀 Throttling & Debouncing
❓ Debounce Example
function debounce(fn, delay) {
  let timer;
  return function(...args) {
    clearTimeout(timer);
    timer = setTimeout(() => fn.apply(this, args), delay);
  };
}

window.addEventListener("resize", debounce(() => {
  console.log("Debounced resize");
}, 300));

❓ Throttle Example
function throttle(fn, limit) {
  let last = 0;
  return function(...args) {
    let now = Date.now();
    if (now - last >= limit) {
      fn.apply(this, args);
      last = now;
    }
  };
}

window.addEventListener("scroll", throttle(() => {
  console.log("Throttled scroll");
}, 500));


✅ That completes Part 4 in .md format.
