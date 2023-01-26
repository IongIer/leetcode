from collections import deque
from pprint import pprint

board = [[-1,1,2,-1],[2,13,15,-1],[-1,10,-1,-1],[-1,6,2,8]]
def snakesAndLadders(board: list[list[int]]) -> int:
    def build_array(board):
        snake = []
        i = 0
        while board:
            curr = board.pop()
            if i % 2 == 0:
                for elem in curr:
                    if elem != -1:
                        snake.append(elem - 1)
                    else:
                        snake.append(len(snake))
            else:
                while curr:
                    pos = curr.pop()
                    if pos != -1:
                        snake.append(pos - 1)
                    else:
                        snake.append(len(snake))
            i += 1
        return snake
    snake = build_array(board)
    print(snake)
    def bfs(snake):
        queue = deque()
        seen = {0}
        steps = 1
        for i in range(1, min(7, len(snake))):
            queue.append(snake[i])
            seen.add(i)
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                print(curr, steps, snake[-1])
                if curr == snake[-1]:
                    return steps
                for i in range(curr + 1, min(curr + 7, len(snake))):
                    if i not in seen:
                        queue.append(snake[i])
                        seen.add(i)
            steps +=1
        return -1
    return bfs(snake)

for x in board:
    print(x)
print(snakesAndLadders(board))