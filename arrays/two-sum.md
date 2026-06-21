# 1. Two Sum

**Difficulty:** Easy
**Topic:** Array, Hash Table
**LeetCode:** https://leetcode.com/problems/two-sum/

## Problem

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

Each input has exactly one solution, and the same element cannot be used twice.

## Example

```python
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
```

Explanation:

```python
nums[0] + nums[1] = 2 + 7 = 9
```

## Approach

Use a hash map to store numbers we have already seen.

For each number `num`, calculate:

```python
need = target - num
```

If `need` already exists in the hash map, then we have found the two numbers.

Otherwise, store the current number and its index in the hash map.

## Python Solution

```python
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            need = target - num

            if need in seen:
                return [seen[need], i]

            seen[num] = i
```

## Complexity

**Time Complexity:** `O(n)`

We loop through the list once.

**Space Complexity:** `O(n)`

We store numbers in a hash map.
