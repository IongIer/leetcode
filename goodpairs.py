from typing import List
from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)
        answer = 0
        for c in count:
            if count[c] > 1:
                answer += (count[c] * (count[c] - 1)) // 2
        return answer