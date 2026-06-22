# 4. Median of Two Sorted Arrays

## Problem

Given two sorted arrays `nums1` and `nums2` of size `m` and `n`, return the median of the two sorted arrays.

The overall run time complexity should be `O(log(m + n))`.

## Examples

### Example 1

```text
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
```

### Example 2

```text
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
```

## Approach

Use binary search on the smaller array.

Instead of merging both arrays, we split the two arrays into a left half and a right half.

The correct split must satisfy:

```text
max(left side) <= min(right side)
```

For two arrays, this means:

```text
max_left1 <= min_right2
max_left2 <= min_right1
```

Once the split is correct:

- If the total length is odd, the median is the largest value on the left side.
- If the total length is even, the median is the average of the largest value on the left side and the smallest value on the right side.

## Complexity

```text
Time Complexity: O(log(min(m, n)))
Space Complexity: O(1)
```

Where `m` and `n` are the lengths of `nums1` and `nums2`.

## Code

```python
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Always binary search the smaller array.
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total_left = (m + n + 1) // 2

        left, right = 0, m

        while left <= right:
            partition1 = (left + right) // 2
            partition2 = total_left - partition1

            max_left1 = float("-inf") if partition1 == 0 else nums1[partition1 - 1]
            min_right1 = float("inf") if partition1 == m else nums1[partition1]

            max_left2 = float("-inf") if partition2 == 0 else nums2[partition2 - 1]
            min_right2 = float("inf") if partition2 == n else nums2[partition2]

            if max_left1 <= min_right2 and max_left2 <= min_right1:
                if (m + n) % 2 == 1:
                    return float(max(max_left1, max_left2))

                return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2

            if max_left1 > min_right2:
                right = partition1 - 1
            else:
                left = partition1 + 1

        return 0.0
```
