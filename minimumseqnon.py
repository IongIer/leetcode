# Given the array nums, obtain a subsequence of the array whose sum of elements is strictly greater than the sum of the non included elements in such subsequence.

# If there are multiple solutions, return the subsequence with minimum size and if there still exist multiple solutions, return the subsequence with the maximum total sum of all its elements. A subsequence of an array can be obtained by erasing some (possibly zero) elements from the array.

# Note that the solution with the given constraints is guaranteed to be unique. Also return the answer sorted in non-increasing order.

from typing import List

# My initial solution


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        ordered = sorted(nums)
        index = -1
        while True:
            if sum(ordered[index:]) > sum(ordered[:index]):
                return reversed(ordered[index:])
            index -= 1
