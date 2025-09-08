# Web Workers – Heavy Lifting Example
<details> <summary>👉 Answer</summary>

✅ Main thread (index.html + script.js):

```html
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
```

```js

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
```

</details>


Web Workers – Real-World Example (Image Processing)
<details> <summary>👉 Answer</summary>

✅ Main thread (index.html + script.js):

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Web Worker Image Processing</title>
</head>
<body>
  <h2>Web Worker – Grayscale Image</h2>
  <input type="file" id="upload" accept="image/*" />
  <canvas id="canvas"></canvas>

  <script>
    const canvas = document.getElementById("canvas");
    const ctx = canvas.getContext("2d");
    let worker;

    document.getElementById("upload").addEventListener("change", (e) => {
      const file = e.target.files[0];
      if (!file) return;

      const img = new Image();
      img.onload = () => {
        canvas.width = img.width;
        canvas.height = img.height;
        ctx.drawImage(img, 0, 0);

        // Get image data
        const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);

        // Create Worker
        if (!worker) worker = new Worker("imageWorker.js");

        // Receive processed data
        worker.onmessage = (event) => {
          ctx.putImageData(event.data, 0, 0);
        };

        // Send image data to worker
        worker.postMessage(imageData);
      };
      img.src = URL.createObjectURL(file);
    });
  </script>
</body>
</html>
```

```js
✅ Worker thread (imageWorker.js):

// imageWorker.js
self.onmessage = function(event) {
  const imageData = event.data;
  const data = imageData.data;

  for (let i = 0; i < data.length; i += 4) {
    // RGB average for grayscale
    const avg = (data[i] + data[i+1] + data[i+2]) / 3;
    data[i] = data[i+1] = data[i+2] = avg;
  }

  // Send back processed image
  postMessage(imageData);
};
```

<details>

⚡ How it works:

Main thread loads a large image and extracts pixel data.

Worker receives pixel data and applies grayscale processing in a separate thread.

Main thread receives processed data and updates the canvas without blocking UI.

This approach is great for image filters, canvas manipulations, data-heavy computations, and real-time visualizations.
