from itertools import combinations
from typing import List

## My naive Solution


def twoSum(nums: List[int], target: int) -> List[int]:
    pairs = combinations(nums, 2)
    for combination in pairs:
        if sum(combination) == target:
            first = combination[0]
            second = combination[1]
            first_i = nums.index(first)
            second_i = nums.index(second)
            if first == second:
                return [first_i, nums[first_i + 1 :].index(second) + first_i + 1]
            return [first_i, second_i]


##Efficient solution copied from lc
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]
