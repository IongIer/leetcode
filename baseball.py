from typing import List

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        result = []
        for n in ops:
            match n:
                case "C":
                    result.pop()
                case "D":
                    result.append(result[-1] * 2)
                case "+":
                    result.append(result[-2]+result[-1])
                case other:
                    result.append(int(n))
                
        return sum(result)