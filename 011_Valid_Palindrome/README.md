# 125. Valid Palindrome

**LeetCode:** [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)  
**Difficulty:** Easy  
**Topic:** Two Pointers / String  
**Language:** Python 3

---

## Problem

Given a string `s`, determine whether it is a palindrome after:

1. Converting uppercase letters to lowercase.
2. Removing all non-alphanumeric characters.

A palindrome reads the same forward and backward.

### Examples

```text
Input: s = "A man, a plan, a canal: Panama"
Output: true
```

```text
Input: s = "race a car"
Output: false
```

```text
Input: s = " "
Output: true
```

---

## Approach: Two Pointers

1. Initialize `left` at the beginning and `right` at the end.
2. Skip non-alphanumeric characters.
3. Compare the lowercase versions of the characters at both pointers.
4. If they differ, return `False`.
5. If they match, move both pointers inward.
6. If all comparisons succeed, return `True`.

---

## Solution

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1

        return True
```

---

## Complexity

- **Time:** O(n) — Each pointer moves through the string at most once.
- **Auxiliary Space:** O(1) — Uses only two pointers and temporary character comparisons.

---

## Key Learnings

- Two Pointers technique.
- String traversal from both ends.
- `isalnum()` to identify letters and numbers.
- `lower()` for case-insensitive comparison.
- Skipping spaces and punctuation.
- Handling empty strings after filtering.

---

## Status

- [x] Problem understood
- [x] Two Pointers implemented
- [x] Edge cases considered
- [x] Complexity analyzed
- [x] README documented