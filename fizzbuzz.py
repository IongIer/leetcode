from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fizbuz = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                fizbuz.append("FizzBuzz")
                continue
            if i % 3 == 0:
                fizbuz.append("Fizz")
                continue
            if i % 5 ==0:
                fizbuz.append("Buzz")
                continue
            fizbuz.append(str(i))
        return fizbuz
        