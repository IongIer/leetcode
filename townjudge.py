from typing import List
from collections import defaultdict


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        hash = defaultdict(set)
        for x, y in trust:
            hash[x].add(y)
        amount = len(hash)
        if amount == n or amount - n < -1:
            return -1
        for i in range(1, n + 1):
            if i not in hash:
                for x in hash.values():
                    if i not in x:
                        break
                else:
                    return i
        return -1
