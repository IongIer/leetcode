from collections import deque
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]):
        answer = deque()
        queue = deque(intervals)
        while queue:
            current = queue.popleft()
            if newInterval[1] < current[0]:
                answer.append(newInterval)
                answer.append(current)
                return answer + queue
            if newInterval[0] > current[1]:
                answer.append(current)
            else:
                newInterval = [
                    min(newInterval[0], current[0]),
                    max(newInterval[1], current[1]),
                ]
        if not queue:
            answer.append(newInterval)
            return answer
