from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        total = 0
        largest = max(costs)
        count_map = [0] * (largest + 1)
        print(len(count_map))
        for cost in costs:
            count_map[cost] += 1
        for i, v in enumerate(count_map):
            if v == 0:
                pass
            for _ in range(v):
                if coins >= i:
                    coins -= i
                    total += 1
        return total
        
