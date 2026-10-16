# 21 Days of Problem Solving with JavaScript

A 21-day, self-paced curriculum that builds problem-solving skill in JavaScript from
scratch — starting with loops and arithmetic, ending with binary search trees.

Each day is one folder containing the day's **core concept focus**, a **questions list**,
and (for most days) a **homework / practice challenge** set. Concept-heavy days also ship
explanatory notes.

> **Status:** this repository currently holds the curriculum — problem statements and
> notes. Solutions are written per-day as you work through them; add them inside the
> matching `Day-*` folder.

## Curriculum

| Day | Topic | Files |
| --- | --- | --- |
| 1 | Simple Number Problems | [questions](Day-1_simple-number-problems/questions.md) |
| 2 | Conditions & Logic | [questions](Day-2_conditions-and-logic/questions.md) |
| 3 | Loops & Patterns | [questions](Day-3_loops-and-patterns/questions.md) |
| 4A | Understanding the Decimal Number System | [questions](Day-4a_understanding-decimal-number-system/questions.md) |
| 4B | Digits & Numbers | [questions](Day-4b_digits-and-numbers/questions.md) |
| 5 | Factors & Multiples (HCF / LCM) | [questions](Day-5_factors-and-multiples/questions.md) |
| 6 | Prime & Fibonacci | [questions](Day-6_prime-and-fibonacci/questions.md) |
| 7 | Prime Factorization & Composite Numbers | [questions](Day-7_prime-factorization/questions.md) |
| 8 | String Problems (basics) | [questions](Day-8_string-basic-questions/questions.md) |
| 9 | Medium String Algorithms | [questions](Day-9_string-intermediate-questions/questions.md) |
| 10 | Arrays — Basics | [questions](Day-10_basic-array-questions/questions.md) |
| 11 | Medium Array Problems | [questions](Day-11_medium-array-questions/questions.md) |
| 12 | Bubble Sort | [questions](Day-12_bubble-sort/questions.md) |
| 13 | Selection Sort | [questions](Day-13_selection-sort/questions.md) |
| 14 | Insertion Sort | [questions](Day-14_insertion-sort/questions.md) |
| 15 | Linear Search | [questions](Day-15_linear-search/questions.md) |
| 16 | Binary Search | [questions](Day-16_binary-search/questions.md) |
| 17 | Introduction to Recursion | [questions](Day-17_introduction-to-recursion/questions.md) |
| 18 | Recursion on Arrays & Strings | [questions](Day-18_recursion-on-arrays-and-strings/questions.md) |
| 19 | Recursion on Objects | [questions](Day-19_recursion-on-objects/questions.md) |
| 20 | Trees & Tree Traversal | [notes](Day-20_trees-in-javascript/trees.md) · [questions](Day-20_trees-in-javascript/questions.md) |
| 21 | Binary Search Trees | [notes](Day-21_binary-search-trees/types-of-trees.md) · [assignment](Day-21_binary-search-trees/assignment.md) |

## Learning Path

1. **Days 1–3 — Foundations:** loops, conditionals, nested loops, pattern printing.
2. **Days 4–7 — Number theory:** digit extraction with `%` and `/`, factors, multiples,
   HCF/LCM, primes, Fibonacci, prime factorization.
3. **Days 8–9 — Strings:** traversal, frequency maps, sliding window, substring search.
4. **Days 10–11 — Arrays:** aggregation, two pointers, prefix sums.
5. **Days 12–16 — Sorting & searching:** bubble, selection, insertion sort; linear and
   binary search.
6. **Days 17–19 — Recursion:** base vs. recursive case, index-driven recursion,
   depth-first traversal of nested objects.
7. **Days 20–21 — Trees:** tree terminology and traversal, general/binary/BST types,
   BST insert, search and delete.

## How to Use This Repo

1. Open the day's folder and read the **Core Concept Focus** before looking at problems.
2. Solve every question in the **Questions List** yourself — no copying — then do the
   **Homework / Practice Challenge**.
3. Save your work next to the questions, e.g.
   `Day-1_simple-number-problems/solutions/01-print-1-to-n.js`.
4. For each solution, state its **time and space complexity** in a comment. From Day 12
   onward this is the point of the exercise, not an extra.
5. Move on only when you can re-solve the day's problems from a blank file.

## Running Your Solutions

Any JavaScript runtime works; no dependencies, no build step.

```bash
node Day-1_simple-number-problems/solutions/01-print-1-to-n.js
```

## Conventions

- One folder per day: `Day-<n>_<kebab-case-topic>`.
- Problem statements live in `questions.md`; conceptual explainers get their own file
  (`trees.md`, `types-of-trees.md`).
- Each problem states **Input**, **Output**, and the skill it teaches.
