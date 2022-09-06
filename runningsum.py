# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running = []
        last = sum(nums)
        for val in nums[::-1]:
            running.append(last)
            last -= val
        return running[::-1]
