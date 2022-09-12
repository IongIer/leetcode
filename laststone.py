import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        inverted = [-x for x in stones]
        heapq.heapify(inverted)
        while inverted:
            try:
                if inverted[0] == inverted[1]:
                    heapq.heappop(inverted)
                    heapq.heappop(inverted)
                else:
                    first = abs(heapq.heappop(inverted))
                    second = abs(heapq.heappop(inverted))
                    heapq.heappush(inverted, -(first - second))
            except IndexError:
                return abs(inverted[0])
        return 0
