# 🎯 **Day 20 – Trees & Tree Traversal**

---

## 🌳 **Given Tree Structure (Use This for All Non-XML Questions)**

```python
media_tree = {
    "name": "media",
    "children": [
        {
            "name": "images",
            "children": [
                {
                    "name": "events",
                    "children": [
                        {
                            "name": "birthday",
                            "children": [
                                {"name": "cake.png", "children": []},
                                {"name": "party.jpg", "children": []},
                            ],
                        },
                    ],
                },
                {
                    "name": "wallpapers",
                    "children": [
                        {"name": "nature.jpg", "children": []},
                        {"name": "city.png", "children": []},
                    ],
                },
            ],
        },
        {
            "name": "music",
            "children": [
                {
                    "name": "rock",
                    "children": [{"name": "song1.mp3", "children": []}],
                },
            ],
        },
        {
            "name": "videos",
            "children": [],
        },
    ],
}
```

---

## 📄 **Given XML Document (Use This for All XML Questions)**

Python has no DOM, but `xml.etree.ElementTree` gives you the same shape: a root
element, child elements, tags, and attributes.

```python
import xml.etree.ElementTree as ET

document = ET.fromstring(
    """
    <html>
      <body>
        <div id="app">
          <div class="row">
            <span>hello</span>
            <span>world</span>
          </div>
          <div class="row">
            <p>text</p>
          </div>
        </div>
        <footer><span>end</span></footer>
      </body>
    </html>
    """
)

body = document.find("body")
```

Each element is iterable over its children: `for child in element: ...`
Tag name is `element.tag`, attributes come from `element.get("id")`.

---

## 🏫 **Class Questions**

---

### **1️⃣ Print All Node Names in the Tree (Depth-First Order)**

Print all the `"name"` values using recursion

---

### **2️⃣ Count the Total Number of Nodes in the Tree**

Total count (including root)

---

### **3️⃣ Print Only Leaf Nodes**

Print names of nodes that have no children

---

### **4️⃣ XML: Print All Tag Names Inside `document` (DFS)**

_Input:_ `document`  
Print tag names of all elements  
Constraint: recursion only. No `document.iter()` and no `document.findall(".//*")`

---

### **5️⃣ XML: Count Total Number of Elements Inside `body`**

_Input:_ `body`  
Total element count

---

## 🏠 **Homework Questions**

---

### **1️⃣ Count Total Number of Leaf Nodes in the Tree**

Number of leaf nodes

---

### **2️⃣ Find the Maximum Depth of the Tree**

Maximum depth value

---

### **3️⃣ Find the Height of the Tree**

Height of the tree

---

### **4️⃣ Check If a Folder or File Exists in the Tree**

`True` or `False`

---

### **5️⃣ Print the Path to a Given File**

`media → images → wallpapers → city.png`

---

### **6️⃣ XML: Print Only Leaf Elements**

_Input:_ `body`  
Elements that have no child elements

---

### **7️⃣ XML: Count How Many Times a Specific Tag Appears**

_Input:_ `body`, tag = `"div"`  
Count of `<div>` elements

---

### **8️⃣ XML: Find the Maximum Depth of the Document**

_Input:_ `body`  
Maximum nesting depth

---

### **9️⃣ XML: Check If an Element With a Given ID Exists**

_Input:_ `body`, id = `"app"`  
`True` or `False`  
Constraint: manual recursive traversal
