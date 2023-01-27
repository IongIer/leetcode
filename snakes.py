from collections import deque


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

    def bfs(snake):
        queue = deque()
        seen = {0}
        steps = 0
        queue.append(snake[0])
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
            steps += 1
        return -1

    return bfs(snake)


snake = build_array(board)

print(snakesAndLadders(board))
