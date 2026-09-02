# Shared Course Resources

This folder contains shared CSS styles and JavaScript for HTML lessons.

```text
assets/
├── css/
│   └── course.css
└── js/
    └── course.js
```

Include them in lesson HTML files:

```html
<link rel="stylesheet" href="../assets/css/course.css">
<script src="../assets/js/course.js" defer></script>
```

The root `index.html` uses `course.js` to load `state.json` and render the progress summary dashboard.
