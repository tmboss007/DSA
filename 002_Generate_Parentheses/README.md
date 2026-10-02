# Generate Parentheses

**Platform:** LeetCode  
**Problem:** 22  
**Difficulty:** Medium  
**Topic:** Recursion, Backtracking

---

## Problem

Given `n` pairs of parentheses, generate all combinations
of well-formed parentheses.

## Example

### Input

n = 3

### Output

[
    "((()))",
    "(()())",
    "(())()",
    "()(())",
    "()()()"
]

## Approach

Use backtracking to build the parentheses string.

We keep track of:

- `open` → number of opening brackets used
- `close` → number of closing brackets used

Rules:

1. We can add `(` if `open < n`
2. We can add `)` if `close < open`
3. When `open == n` and `close == n`,
   we have a complete valid combination.

## Complexity

Time: O(...)
Space: O(...)

## Key Learning

This problem helped me understand:

- Recursion
- Backtracking
- Recursive decision trees
- Pruning invalid possibilities