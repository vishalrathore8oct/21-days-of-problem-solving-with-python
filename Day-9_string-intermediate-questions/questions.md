# 🎯 **Day 9 – Medium String Algorithms**

### 🧩 **Core Concept Focus**

- Sliding window problems
- Substring search
- Window expansion & contraction
- Character frequency dictionaries

---

# 🏫 **Class Questions**

---

### **1️⃣ Find if One String Is a Substring of Another (Manual Method)**

- **Input:**
  Main string: `"hellothere"`
  Target string: `"there"`

- **Output:**
  `True`
  ✨ _Manual parsing only; check character by character without using the `in` operator or `str.find()`._

---

### **2️⃣ Manual Substring Search (Without Using `str.find()`)**

- **Input:** text = `"hello world"`, pattern = `"wor"`
- **Output:** `Found at index 6`
  ✨ _Classic naive pattern matching algorithm (two nested loops)._

---

### **3️⃣ Check if One String is Rotation of Another**

- **Input:** `"abcde"`, `"cdeab"`
- **Output:** `Rotation`
  ✨ _Use the trick: second string must be inside `(s1 + s1)`._

---

# 🏠 **Homework Questions**

---

### **1️⃣ Count Frequency of Each Word in a Sentence**

- **Input:** `"i love coding and i love python"`
- **Output:** `{'i': 2, 'love': 2, 'coding': 1, 'and': 1, 'python': 1}`
  ✨ _Word parsing + dictionary building._

---

### **2️⃣ Check If a String Is a Pangram**

- **Input:** `"The quick brown fox jumps over the lazy dog"`
- **Output:** `Pangram`
  ✨ _Check if all 26 letters exist._

---

### **3️⃣ Remove All Duplicate Words From a Sentence**

- **Input:** `"this is is a test test string"`
- **Output:** `"this is a test string"`
  ✨ _Track seen words, build cleaned sentence._

---

### **4️⃣ Find the Longest Palindromic Substring (Brute Force Allowed)**

- **Input:** `"babad"`
- **Output:** `"bab"` or `"aba"`
  ✨ _Check all substrings; teaches brute-force reasoning._

---

### **5️⃣ Find All Anagram Pairs in a List of Strings**

- **Input:** `["cat", "tac", "act", "dog"]`
- **Output:** `["cat", "tac", "act"]`

---

### **6️⃣ Find the Longest Substring Without Repeating Characters (Sliding Window)**

- **Input:** `"abcabcbb"`
- **Output:** `"abc"`
  ✨ _Introduction to sliding windows, dictionaries, and window shrinking logic._
