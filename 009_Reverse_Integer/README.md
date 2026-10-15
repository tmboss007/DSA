# 7. Reverse Integer

**LeetCode:** [Reverse Integer](https://leetcode.com/problems/reverse-integer/)  
**Difficulty:** Medium  
**Topic:** Math  
**Language:** Python 3

---

## Problem

Given a signed 32-bit integer `x`, reverse its digits.

If the reversed number falls outside the range `[-2147483648, 2147483647]`, return `0`.

### Examples

```text
Input: x = 123
Output: 321
```

```text
Input: x = -123
Output: -321
```

```text
Input: x = 120
Output: 21
```

---

## Approach

1. Store the sign of the original number.
2. Convert the number to its absolute value.
3. Extract the last digit using `% 10`.
4. Remove the last digit using `// 10`.
5. Append the digit to the reversed number.
6. Check for overflow before updating the result.
7. Restore the original sign and return the result.

---

## Solution

```python
class Solution:
    def reverse(self, x: int) -> int:

        sign = -1 if x < 0 else 1
        x = abs(x)

        result = 0
        limit = 2147483647 if sign == 1 else 2147483648

        while x > 0:
            digit = x % 10
            x //= 10

            if result > limit // 10 or (
                result == limit // 10 and digit > limit % 10
            ):
                return 0

            result = result * 10 + digit

        return result * sign
```

---

## Complexity

- **Time:** O(log |x|) — Processes each digit once.
- **Space:** O(1) — Uses a constant number of variables.

---

## Key Learnings

- Digit extraction using `% 10`.
- Removing digits using `// 10`.
- Reversing a number mathematically.
- Handling negative integers.
- Checking signed 32-bit integer overflow.

---

## Status

- [x] Problem understood
- [x] Solution implemented
- [x] Overflow handled
- [x] Complexity analyzed
- [x] README documented