# Search an Element in an Array

## Problem

Given an array `A` of size `N` and an element `X`,
check whether `X` exists in the array.

Return:

- `YES` if `X` exists
- `NO` otherwise

## Example

### Input

5 3
7 3 5 2 1

### Output

YES

## Approach

We traverse the array and check each element against `X`.

If we find `X`, we return `YES`.

If we reach the end without finding it, we return `NO`.

This is called Linear Search.

## Complexity

- Time: O(N)
- Space: O(1)

## What I Learned

- Array traversal
- Linear search
- Python `in` operator