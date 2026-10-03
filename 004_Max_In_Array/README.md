# Find maximum in an Array (CodeChef)

## Problem Statement
Given a list of $N$ integers, representing the heights of mountains, find the height of the tallest mountain.

**Input:**
* The first line will contain $T$, the number of testcases. Then the testcases follow.
* The first line in each testcase contains one integer, $N$.
* The following line contains $N$ space-separated integers: the height of each mountain.

**Output:**
* For each testcase, output one line with one integer: the height of the tallest mountain for that test case.

**Constraints:**
* $1 \leq T \leq 10$
* $1 \leq N \leq 100000$
* $0 \leq \text{height of each mountain} \leq 10^9$

---

## Approach: "King of the Hill" (Linear Search)
Since the array is unsorted, we must check every single element at least once to guarantee we have found the absolute largest number. This gives us a time complexity of $O(N)$.

1. **Initialize:** Assume the very first mountain in the list is the tallest one seen so far and store its height in a tracking variable.
2. **Iterate:** Loop through the rest of the mountain heights one by one.
3. **Compare:** For each mountain, check if its height is strictly greater (`>`) than the current record.
4. **Update:** If the current mountain is taller, update the tracking variable to this new height.
5. **Output:** Once the loop finishes checking all elements, the tracking variable will hold the maximum height.
