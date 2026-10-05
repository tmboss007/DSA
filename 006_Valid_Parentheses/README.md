# Valid Parentheses

**LeetCode #20 — Easy**

## Problem

Given a string `s` containing only `()[]{}`, determine if the brackets are valid.

A valid string must:

* Have matching opening and closing brackets.
* Close brackets in the correct order.
* Have every closing bracket paired with an opening bracket.

### Examples

```text
"()"       → True
"()[]{}"   → True
"(]"       → False
"([])"     → True
"([)]"     → False
```

## Approach

Use a **Stack** because brackets must be closed in reverse order of opening.

* Push every opening bracket into the stack.
* For a closing bracket, check if it matches the top of the stack.
* If it doesn't match or the stack is empty, return `False`.
* At the end, return `True` only if the stack is empty.

## Python Solution

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char in pairs:
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)

        return not stack
```

## Complexity

* **Time:** `O(n)`
* **Space:** `O(n)`

## Key Concept

**Stack (LIFO)** — the most recently opened bracket must be the first one to close.

## Learning

This problem helped me understand how **stacks** can be used to solve nested and matching-bracket problems efficiently.
