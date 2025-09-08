Web Workers – Heavy Lifting Example
<details> <summary>👉 Answer</summary>

✅ Main thread (index.html + script.js):

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Web Worker Example</title>
</head>
<body>
  <h2>Web Worker – Heavy Computation</h2>
  <button id="start">Start Worker</button>
  <p id="result"></p>

  <script>
    let worker;

    document.getElementById("start").addEventListener("click", () => {
      if (window.Worker) {
        worker = new Worker("worker.js"); // create worker

        // receive message from worker
        worker.onmessage = function(event) {
          document.getElementById("result").textContent = 
            "Sum of numbers: " + event.data;
        };

        // send data to worker
        worker.postMessage(1000000000); // heavy number
      } else {
        alert("Web Workers are not supported in this browser.");
      }
    });
  </script>
</body>
</html>


✅ Worker thread (worker.js):

// worker.js
self.onmessage = function(event) {
  let n = event.data;
  let sum = 0;

  // Heavy computation (loop)
  for (let i = 0; i < n; i++) {
    sum += i;
  }

  // Send result back to main thread
  postMessage(sum);
};


⚡ How it works:

Main thread creates a Worker (new Worker("worker.js")).

Worker does heavy computation (sum of 1 billion numbers).

Result is sent back via postMessage without freezing UI.

</details>
