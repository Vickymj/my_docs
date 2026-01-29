---
id: html_notes
title: HTML  Notes
---

# HTML – Complete Deep Reference

---

## 1. What is HTML?
HTML (HyperText Markup Language) is the backbone of web pages.
It defines:
- Page **structure**
- **Content layout**
- **Semantic meaning**

HTML works with:
- **CSS** → Styling
- **JavaScript** → Interactivity

---

## 2. HTML Document Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="HTML Deep Notes">
  <title>HTML Guide</title>
</head>
<body>
  <header>Header</header>
  <main>Main Content</main>
  <footer>Footer</footer>
</body>
</html>
```

---

## 3. HTML Elements & Tags
- Opening tag `<p>`
- Content
- Closing tag `</p>`

### Empty Tags
```html
<br>
<hr>
<img>
<input>
```

---

## 4. HTML Attributes
```html
<p id="para1" class="text" title="tooltip">Hello</p>
```

Common attributes:
- `id`
- `class`
- `style`
- `title`
- `hidden`
- `data-*`

---

## 5. Headings & Paragraphs

```html
<h1>Main Heading</h1>
<h2>Sub Heading</h2>
<p>This is a paragraph.</p>
```

Best practice:
- One `<h1>` per page

---

## 6. Text Formatting

```html
<b>Bold</b>
<strong>Important</strong>
<i>Italic</i>
<em>Emphasis</em>
<mark>Highlight</mark>
<small>Small</small>
<del>Deleted</del>
<ins>Inserted</ins>
<sub>H2O</sub>
<sup>2</sup>
```

---

## 7. Links & Anchors

```html
<a href="https://example.com" target="_blank">Visit</a>
<a href="#section1">Jump</a>
```

Target values:
- `_self`
- `_blank`
- `_parent`
- `_top`

---

## 8. Images

```html
<img src="img.png" alt="Description" width="200">
```

Accessibility:
- Always use `alt`

---

## 9. Lists

### Unordered
```html
<ul>
  <li>HTML</li>
  <li>CSS</li>
</ul>
```

### Ordered
```html
<ol>
  <li>Design</li>
  <li>Develop</li>
</ol>
```

### Description
```html
<dl>
  <dt>HTML</dt>
  <dd>Markup Language</dd>
</dl>
```

---

## 10. Tables

```html
<table border="1">
  <caption>Employees</caption>
  <thead>
    <tr>
      <th>Name</th>
      <th>Role</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>John</td>
      <td>Dev</td>
    </tr>
  </tbody>
</table>
```

### Colspan & Rowspan
```html
<td colspan="2">Total</td>
<td rowspan="2">Merged</td>
```

---

## 11. Block vs Inline

Block:
```html
<div>Block</div>
<p>Paragraph</p>
```

Inline:
```html
<span>Inline</span>
<a>Link</a>
```

---

## 12. Semantic HTML (IMPORTANT)

```html
<header></header>
<nav></nav>
<section></section>
<article></article>
<aside></aside>
<footer></footer>
```

Benefits:
- SEO
- Accessibility
- Readability

---

## 13. HTML Forms (DEEP)

### Basic Form
```html
<form action="/submit" method="post">
  <label>Name:</label>
  <input type="text" name="name">
  <button type="submit">Submit</button>
</form>
```

### Input Types
```html
<input type="text">
<input type="email">
<input type="password">
<input type="number">
<input type="date">
<input type="file">
<input type="hidden">
```

---

## 14. Radio Buttons

```html
<label>
  <input type="radio" name="gender" value="male"> Male
</label>
<label>
  <input type="radio" name="gender" value="female"> Female
</label>
```

Rule:
- Same `name` → one selection

---

## 15. Checkboxes

```html
<label>
  <input type="checkbox" name="skills" value="html"> HTML
</label>
<label>
  <input type="checkbox" name="skills" value="css"> CSS
</label>
```

Multiple selections allowed.

---

## 16. Dropdown (Select)

```html
<select name="country">
  <option value="">Select</option>
  <option value="in">India</option>
  <option value="us">USA</option>
</select>
```

### Grouped Options
```html
<optgroup label="Asia">
  <option>India</option>
</optgroup>
```

---

## 17. Textarea

```html
<textarea rows="4" cols="30">
Enter text
</textarea>
```

---

## 18. Form Attributes

```html
<input type="text" required minlength="3" maxlength="10">
```

Important attributes:
- `required`
- `readonly`
- `disabled`
- `placeholder`
- `pattern`
- `autofocus`

---

## 19. Validation Example

```html
<input type="email" required>
```

Browser validates automatically.

---

## 20. Media Elements

### Video
```html
<video controls width="300">
  <source src="movie.mp4" type="video/mp4">
</video>
```

### Audio
```html
<audio controls>
  <source src="song.mp3" type="audio/mpeg">
</audio>
```

---

## 21. iframe

```html
<iframe src="https://example.com" width="400"></iframe>
```

---

## 22. HTML Comments

```html
<!-- Comment -->
```

---

## 23. File Paths

```html
<img src="img.jpg">
<img src="images/img.jpg">
<img src="../img.jpg">
```

---

## 24. Accessibility Basics
- Use `<label>` with inputs
- Use semantic tags
- Use `alt`
- Use `aria-label`

---

## 25. Best Practices
- Semantic HTML
- Clean indentation
- Avoid inline styles
- One `<h1>` per page
- Mobile friendly

---

## 26. Interview Notes
- Difference between `div` & `span`
- GET vs POST
- Required vs disabled
- Semantic HTML benefits
- Radio vs checkbox

---

✅ **Complete HTML deep notes – forms, dropdowns, radio, validation, semantic & interview ready**
