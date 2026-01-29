---
id: docusaurus-all-features
title: Docusaurus Documentation – All Features Template
description: Complete reference template with all Docusaurus documentation features
sidebar_position: 1
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# 📘 Docusaurus Documentation – Complete Template

This file demonstrates **ALL features available in Docusaurus documentation**.
Use it as a **master template** for any technical skill.

---

## 🧾 Front Matter (Metadata)

Controls sidebar, title, SEO, and routing.

```md
---
id: example-id
title: Example Page
description: Example description
sidebar_position: 1
---
```

---

## 📝 Text Formatting

- **Bold**
- *Italic*
- ~~Strikethrough~~
- `Inline code`

> This is a blockquote

---

## 📋 Lists

### Unordered
- Item A
- Item B
  - Sub Item

### Ordered
1. One
2. Two
3. Three

---

## 📊 Tables

| Feature | Supported | Notes |
|------|---------|------|
| Tables | Yes | Markdown |
| Tabs | Yes | MDX |
| Admonitions | Yes | Built-in |
| Code Highlight | Yes | Prism |

---

## 💡 Admonitions

:::info
This is an **info** admonition.
:::

:::tip
This is a **tip** admonition (green).
:::

:::warning
This is a **warning** admonition.
:::

:::danger
This is a **danger** admonition.
:::

---

## 🧩 Expand / Collapse Section

<details>
<summary><strong>Click to expand</strong></summary>

This content is hidden by default.

```bash
echo "Expandable content"
```

</details>

---

## 💻 Code Blocks

```js title="example.js"
console.log("Hello Docusaurus");
```

### Highlight Lines

```js {2,4}
const a = 10;
const b = 20;
const sum = a + b;
console.log(sum);
```

---

## 🧪 Tabs Example

<Tabs>
<TabItem value="linux" label="Linux">

```bash
sudo apt install git
```

</TabItem>

<TabItem value="windows" label="Windows">

```powershell
choco install git
```

</TabItem>

<TabItem value="mac" label="MacOS">

```bash
brew install git
```

</TabItem>
</Tabs>

---

## 🖼 Images

```md
![Alt Text](./img/example.png)
```

---

## 🔗 Internal Links

```md
[Go to Git Docs](./git.md)
```

---

## 🏗 Folder Structure

```text
docs/
├── intro.md
├── git/
│   └── git.md
├── docker/
│   └── docker.md
└── linux/
    └── linux.md
```

---

## 📌 Inline Highlights

Use `git status` to check repository state.

---

## 📎 External Links

- [Docusaurus Official Docs](https://docusaurus.io)
- [Markdown Guide](https://www.markdownguide.org)

---

## 🔐 Security Notes

:::warning
Never store secrets directly in documentation.
:::

---

## ✅ Summary

✔ Covers **all Docusaurus documentation features**  
✔ Ready-to-copy template  
✔ Ideal for **technical skill documentation**  

🚀 Happy documenting with Docusaurus!
