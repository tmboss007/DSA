# 35. Search Insert Position

**LeetCode:** [Search Insert Position](https://leetcode.com/problems/search-insert-position/)  
**Difficulty:** Easy  
**Topic:** Binary Search  
**Language:** Python 3

---

## Problem

Given a sorted array of distinct integers and a target, return its index if found. Otherwise, return the index where it should be inserted to maintain sorted order.

The solution must run in **O(log n)** time.

### Examples

```text
Input: nums = [1, 3, 5, 6], target = 5
Output: 2
```

```text
Input: nums = [1, 3, 5, 6], target = 2
Output: 1
```

```text
Input: nums = [1, 3, 5, 6], target = 7
Output: 4
```

---

## Approach: Binary Search

1. Initialize `left = 0` and `right = len(nums) - 1`.
2. Calculate the middle index using `(left + right) // 2`.
3. If the middle element equals the target, return its index.
4. If the middle element is smaller, search the right half.
5. Otherwise, search the left half.
6. If the target is not found, return `left`, which is its correct insertion position.

---

## Solution

```python
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left
```

---

## Complexity

- **Time:** O(log n) — The search area is halved each iteration.
- **Space:** O(1) — Only a constant number of variables are used.

---

## Key Learnings

- Binary Search on sorted arrays.
- Updating `left` and `right` to eliminate half the search area.
- Returning `left` to find the insertion position when the target is absent.

---

## Status

- [x] Problem understood
- [x] Binary Search implemented
- [x] Complexity analyzed
- [x] Solution documented
