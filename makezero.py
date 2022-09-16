from typing import List

# https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nonzero = set(n for n in nums if n != 0)
        return len(nonzero) if nonzero else 0
