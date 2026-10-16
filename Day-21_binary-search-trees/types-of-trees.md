# 🌳 Types of Trees

We will talk about **just 3 types of trees**:

1️⃣ General Tree  
2️⃣ Binary Tree  
3️⃣ Binary Search Tree (BST)  

There are more types but these are the important ones.

---

## 🌱 1️⃣ General Tree

This is the **simplest form of a tree**.

### What it means

* A node can have **any number of children**
* No restriction on structure
* No restriction on ordering

### Key points

* Very flexible
* Easy to represent using nested dictionaries
* Used for:

  * File systems
  * XML / HTML element trees
  * JSON data

👉 We have already used this tree type in Day 20.

---

## 🌲 2️⃣ Binary Tree

Now we add **one simple rule**.

### Rule

👉 Each node can have **at most two children**

* left child
* right child

### Important

* There is **no ordering rule**
* Left child can be bigger or smaller than right

### Example 🌳

```
      10
     /  \
    5    20
```

### Key points

* Structure matters, not values

---

## 🌳 3️⃣ Binary Search Tree (BST)

This is the **most important tree** for problem solving 💡

### Core Rule (Very Important)

For every node:

* All values in the **left subtree** are smaller
* All values in the **right subtree** are greater

This rule applies **recursively**.

### Example 🌲

```
        10
       /  \
      5    15
     / \     \
    2   7     20
```

---

### Why BST Is Powerful 🚀

Because searching becomes **fast**.

At each node:

* Compare value
* Move left or right
* Ignore half of the tree

👉 This is **binary search**, but in tree form.

---

## 🆚 Binary Tree vs BST (Super Important)

| Feature      | Binary Tree | Binary Search Tree |
| ------------ | ----------- | ------------------ |
| Max children | 2           | 2                  |
| Ordering     | ❌ No        | ✅ Yes              |
| Searching    | ❌ Slow      | ✅ Fast             |

---

## 🌐 Real-World Examples

Trees are everywhere 👀

* File systems 📁 → General Tree
* XML / HTML element trees 🌐 → General Tree
* Binary search logic 🔍 → BST