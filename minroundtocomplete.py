from collections import Counter
from typing import List


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        count = Counter(tasks)
        answer = 0
        for k in count:
            if count[k] == 1:
                return -1
            else:
                
                if count[k] % 3 == 0:
                    answer += count[k] // 3
                else:
                    answer += count[k] // 3 + 1

        return answer
        
