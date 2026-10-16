# LeetCode 27 — Remove Element

**Difficulty:** Easy
**Topics:** Array, Two Pointers
**Language:** Python 3
**LeetCode:** [Remove Element](https://leetcode.com/problems/remove-element/)

## Problem Statement

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` from `nums` **in-place** and return the number of elements that are not equal to `val`.

The first `k` elements of `nums` must contain all the elements that are not equal to `val`, where `k` is the returned value.

The order of the remaining elements does not need to change, and the elements beyond the first `k` positions do not matter.

## Example

**Input:**

```python
nums = [3, 2, 2, 3]
val = 3
```

**Output:**

```python
k = 2
nums = [2, 2, _, _]
```

**Explanation:**

Both occurrences of `3` are excluded from the valid portion of the array. The remaining elements are `[2, 2]`, so the function returns `2`.

## Approach: Two Pointers

I used the **Two Pointers** technique to solve this problem without creating an additional array.

* `i` traverses the array and checks each element.
* `k` tracks the position where the next valid element should be placed.
* If `nums[i] != val`, copy the element to `nums[k]` and increment `k`.
* If `nums[i] == val`, skip the element.
* After processing the array, return `k`.

This approach modifies the original array in-place and preserves the relative order of the remaining elements.

## Solution

The implementation is available in [`solution.py`](./solution.py).

## Complexity Analysis

* **Time Complexity:** `O(n)` — Each element is checked once.
* **Space Complexity:** `O(1)` — Only a constant amount of extra space is used.

Here, `n` is the length of the input array.

## Key Learnings

* Understanding in-place array modification.
* Using two pointers to process an array efficiently.
* Moving valid elements to the beginning of an array.
* Handling unwanted elements without creating another array.
* Analyzing time and space complexity.

## Takeaway

This problem helped me understand the **read-and-write pointer** pattern, which is useful for solving other array problems involving removing elements, moving values, and eliminating duplicates.

---

**Part of my DSA journey:** Learning problem-solving patterns through LeetCode using Python 3.
