from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if 2 <= len(nums) and len(nums) <= 10**4:
            if target >= -10**9 and target <= 10**9:
                seen = {}

                for i, num in enumerate(nums):
                    need = target - num

                    if need in seen:
                        return [seen[need], i]

                    seen[num] = i