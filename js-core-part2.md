📘 JavaScript Interview Q&A (Part 2 – Async, Events & Event Loop)

## 17. Event Loop
<details> <summary>👉 Answer</summary>

JavaScript is single-threaded.

The Event Loop checks the **call stack** & **callback queue** to execute tasks.

```js
console.log("Start");

setTimeout(() => console.log("Timeout"), 0);

Promise.resolve().then(() => console.log("Promise"));

console.log("End");
Output:
Start
End
Promise
Timeout
👉 Microtasks (Promises) run before Macrotasks (setTimeout).
```

</details>

## 18. Microtasks vs Macrotasks
<details> <summary>👉 Answer</summary>
Microtasks: executed immediately after current script.
Examples: Promise callbacks, queueMicrotask.

Macrotasks: scheduled tasks.
Examples: setTimeout, setInterval, setImmediate, I/O.

```js
console.log("1");

setTimeout(() => console.log("2"), 0);   // macrotask
Promise.resolve().then(() => console.log("3")); // microtask

console.log("4");
Output:

1
4
3
2
```
</details>

## 19. Timers in JavaScript
<details> <summary>👉 Answer</summary>
setTimeout(fn, delay) → run once after delay.

setInterval(fn, delay) → run repeatedly.

clearTimeout / clearInterval → stop them.

```js

const id = setInterval(() => console.log("Tick"), 1000);

setTimeout(() => clearInterval(id), 5000); // stops after 5s
```
</details>

## 20. Polyfills
<details> <summary>👉 Answer</summary>
A polyfill is a custom implementation of a feature when it's not available in a browser.

👉 Example: Polyfill for Array.prototype.map

```js
if (!Array.prototype.myMap) {
  Array.prototype.myMap = function (callback) {
    let res = [];
    for (let i = 0; i < this.length; i++) {
      res.push(callback(this[i], i, this));
    }
    return res;
  };
}

console.log([1,2,3].myMap(x => x*2)); // [2,4,6]
```
</details>

## 21. Async vs Defer
<details> <summary>👉 Answer</summary>
Async → Script loads in parallel, executes immediately after load.
Defer → Script loads in parallel, executes after HTML parsing is complete.

```js
<script src="script.js" async></script>
<script src="script.js" defer></script>
👉 Use defer for DOM-dependent scripts.
```

</details>

## 22. Debouncing
<details> <summary>👉 Answer</summary>
Debouncing limits function execution → runs only after user stops triggering.

```js
function debounce(fn, delay) {
  let timer;
  return function(...args) {
    clearTimeout(timer);
    timer = setTimeout(() => fn.apply(this, args), delay);
  };
}

const search = debounce((q) => console.log("Searching:", q), 500);

// Simulating user typing
search("a");
search("ab");
search("abc"); // ✅ Only this executes
```
</details>

## 23. Throttling
<details> <summary>👉 Answer</summary>
Throttling ensures function runs at most once in a given interval.

```js
function throttle(fn, delay) {
  let last = 0;
  return function(...args) {
    let now = Date.now();
    if (now - last >= delay) {
      last = now;
      fn.apply(this, args);
    }
  };
}

const log = throttle(() => console.log("Scroll event"), 1000);
window.addEventListener("scroll", log);
```
</details>

## 24. Storage in JS
<details> <summary>👉 Answer</summary>
Cookie → small, sent with HTTP requests (~4KB).

LocalStorage → ~5–10MB, persistent, not sent with requests.

SessionStorage → ~5MB, cleared on tab close.

```js
localStorage.setItem("key", "value");
sessionStorage.setItem("key", "value");
document.cookie = "username=John; max-age=3600";
```
</details>

## 25. Event Propagation
<details> <summary>👉 Answer</summary>

```js
1) Capturing Phase – Event travels top → down


parent.addEventListener("click", handler, true); // capture
2) Target Phase – Event reaches target.

3) Bubbling Phase – Event travels child → parent (default)


parent.addEventListener("click", handler); // bubble
4) stopPropagation – Stops bubbling/capturing


child.addEventListener("click", e => e.stopPropagation());
5) preventDefault – Stops default action (e.g., form submit)


form.addEventListener("submit", e => e.preventDefault());
6) Event Delegation – Use parent to handle child events


document.getElementById("list").addEventListener("click", (e) => {
  if (e.target.tagName === "LI") console.log("Clicked:", e.target.innerText);
});
```

</details> 
