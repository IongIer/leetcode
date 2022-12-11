from collections import deque
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        walk = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        queue = deque()
        entrance = tuple(entrance)
        visited.add(entrance)
        queue.append(entrance)
        distance = 0
        rows, cols = len(maze), len(maze[0])
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                for direction in walk:
                    new = tuple(map(sum, zip(curr, direction)))
                    if curr != entrance:
                        if min(new[0], new[1]) < 0 or new[0] >= rows or new[1] >= cols:
                            return distance
                        else:
                            if new not in visited and maze[new[0]][new[1]] == ".":
                                visited.add(new)
                                queue.append(new)
                            else:
                                visited.add(new)
                    else:
                        if min(new[0], new[1]) < 0 or new[0] >= rows or new[1] >= cols:
                            pass
                        else:
                            if new not in visited and maze[new[0]][new[1]] == ".":
                                visited.add(new)
                                queue.append(new)
                            else:
                                visited.add(new)

            distance += 1
        return -1
