# Let’s prepare CSS + HTML Interview.

## 1. How to center a div vertically in CSS?
<details> <summary>👉 Answer</summary>

Several ways:

Using Flexbox

```css
.parent {
  display: flex;
  align-items: center; /* Vertical center */
  justify-content: center; /* Horizontal center */
  height: 100vh;
}
.child {
  width: 200px;
  height: 100px;
  background: lightblue;
}


Using Grid

.parent {
  display: grid;
  place-items: center;
  height: 100vh;
}


Using Position + Transform

.child {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
```

</details>

## 2. Viewport in HTML
<details> <summary>👉 Answer</summary>

The viewport meta tag controls page dimensions & scaling.
```html

<meta name="viewport" content="width=device-width, initial-scale=1.0">


width=device-width → adapts to device screen width.

initial-scale=1.0 → no zoom initially.

👉 Helps make pages responsive.
```

</details>

## 3. position: relative vs position: absolute
<details> <summary>👉 Answer</summary>

relative → element is positioned relative to its normal position.

absolute → element is positioned relative to the nearest ancestor with position: relative (or the document if none).
```css
.parent {
  position: relative;
}
.child {
  position: absolute;
  top: 10px;
  left: 20px;
}
```

</details>

## 4. LESS vs SCSS
<details> <summary>👉 Answer</summary>

LESS: older, simpler, uses JavaScript-based compiler.

SCSS (Sass): more powerful, advanced features, widely adopted.

```css

👉 Example SCSS:

$color: red;
.box {
  background: $color;
  &:hover { color: white; }
}


👉 Example LESS:

@color: red;
.box {
  background: @color;
  &:hover { color: white; }
}
```

</details>

## 5. HTML5 Tags
<details> <summary>👉 Answer</summary>

Some new semantic HTML5 tags:

```html

<header>

<footer>

<article>

<section>

<nav>

<aside>

<figure> <figcaption>

<video>, <audio>

<canvas>

👉 Adds meaning & improves accessibility.
```

</details>

## 6. Section vs Article
<details> <summary>👉 Answer</summary>

<section> → thematic grouping of content (like chapters, topics).

<article> → independent, reusable content (blog post, news).

```html

<section>
  <h2>Tutorials</h2>
  <article>
    <h3>Learn CSS</h3>
    <p>CSS basics explained...</p>
  </article>
</section>
```

</details>

## 7. Canvas
<details> <summary>👉 Answer</summary>

<canvas> is used for drawing graphics via JavaScript (pixel-based).

```html

<canvas id="myCanvas" width="200" height="100"></canvas>
<script>
let c = document.getElementById("myCanvas");
let ctx = c.getContext("2d");
ctx.fillStyle = "blue";
ctx.fillRect(20, 20, 150, 50);
</script>
```

</details>

## 8. Class vs ID
<details> <summary>👉 Answer</summary>

Class (.class) → reusable across multiple elements.

ID (#id) → unique, used for one element only.

```html

<div class="box"></div>
<div class="box"></div>
<div id="unique"></div>
```

</details>

## 9. Box Model
<details> <summary>👉 Answer</summary>

Each element has 4 layers:

Content → text/image

Padding → space inside border

Border

Margin → space outside
```css
.box {
  width: 200px;
  padding: 10px;
  border: 5px solid black;
  margin: 20px;
}
```

</details>

## 10. Canvas vs SVG
<details> <summary>👉 Answer</summary>

Canvas: pixel-based, better for dynamic animations (games).

SVG: vector-based, scalable, better for static/interactive graphics.

👉 Use SVG for crisp, scalable icons.
👉 Use Canvas for real-time, pixel-heavy rendering.

</details>

## 11. HTML5 Features
<details> <summary>👉 Answer</summary>

Semantic tags (<section>, <article>)

Multimedia (<video>, <audio>)

<canvas> & SVG support

LocalStorage & SessionStorage

Geolocation API

Form enhancements (<datalist>, <input type="email">)

WebSockets, Web Workers

</details>

## 12. Mixins in CSS Preprocessors
<details> <summary>👉 Answer</summary>

Reusable block of CSS.

SCSS Example:
```css
@mixin flexCenter {
  display: flex;
  justify-content: center;
  align-items: center;
}
.box {
  @include flexCenter;
}
```

</details>

## 13. Frameworks in CSS
<details> <summary>👉 Answer</summary>

Bootstrap

Tailwind CSS

Foundation

Bulma

Materialize

</details>

## 14. Browser Compatibility
<details> <summary>👉 Answer</summary>

```css
Use CSS Reset or normalize.css

Use Vendor Prefixes (-webkit-, -moz-)

Use Feature Queries (@supports)

@supports (display: grid) {
  .container { display: grid; }
}
```

</details>

## 15. Responsive Design
<details> <summary>👉 Answer</summary>
```css
Viewport meta tag

Media Queries

Flexbox & Grid

Fluid images

@media (max-width: 600px) {
  .box { width: 100%; }
}
```

</details>

## 16. Flex vs Grid
<details> <summary>👉 Answer</summary>

Flexbox: one-dimensional (row/column).

Grid: two-dimensional (rows + columns).

</details>

## 17. Flex Examples
<details> <summary>👉 Answer</summary>

Sidebar Layout
```css
.container { display: flex; }
.sidebar { width: 200px; }
.main { flex: 1; }


Card Layouts

.cards { display: flex; gap: 10px; }
.card { flex: 1; }


Header/Footer Layouts

.header, .footer { height: 50px; }
.main { flex: 1; }


Navigation Menus

.nav { display: flex; gap: 20px; }
```

</details>

## 18. Grid Examples
<details> <summary>👉 Answer</summary>

Page Layout
```css
.container {
  display: grid;
  grid-template-areas: 
    "header header"
    "sidebar main"
    "footer footer";
  grid-template-columns: 200px 1fr;
}


Image Gallery

.gallery {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
  gap: 10px;
}


Magazine Layout

.magazine {
  display: grid;
  grid-template-columns: 1fr 2fr 1fr;
}
```

</details>

## 19. Meta Tag
<details> <summary>👉 Answer</summary>

Metadata about the document (charset, viewport, SEO).
```html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="Interview prep">
```

</details>

## 20. CSS Variables
<details> <summary>👉 Answer</summary>
```css
:root {
  --main-color: blue;
}
.box {
  color: var(--main-color);
}
```


👉 Variables allow reusability and easier theme changes.

</details>

## 21. Transition vs Transformation
<details> <summary>👉 Answer</summary>

transition → animates property changes.

transform → changes shape, size, position.
```css
.box {
  transition: transform 0.5s;
}
.box:hover {
  transform: rotate(45deg) scale(1.2);
}
```

</details>

## 22. Datalist
<details> <summary>👉 Answer</summary>

Provides autocomplete options in forms.
```html
<input list="browsers">
<datalist id="browsers">
  <option value="Chrome">
  <option value="Firefox">
</datalist>
```

</details>

## 23. lang Attribute
<details> <summary>👉 Answer</summary>

Specifies the language of the document.
```html
<html lang="en">
  <p lang="fr">Bonjour</p>
</html>
```

</details>

## 24. Shadow DOM
<details> <summary>👉 Answer</summary>

Encapsulation of styles & DOM in Web Components.
```html
let shadow = element.attachShadow({ mode: "open" });
shadow.innerHTML = `<style>p{color:red}</style><p>Inside Shadow DOM</p>`;


👉 Styles inside shadow DOM do not leak outside.
```

</details>
