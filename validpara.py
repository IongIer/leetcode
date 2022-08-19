from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        valid_start = "({["
        pairs = {")": "(", "]": "[", "}": "{"}
        if len(s) % 2 == 0:
            stack = deque()
            if s[0] not in valid_start:
                return False
            for i, v in enumerate(s):
                if v in valid_start:
                    stack.append(v)
                else:
                    try:
                        rem = stack.pop()
                        if rem != pairs[v]:
                            return False
                    except IndexError:
                        return False
            return not len(stack)

        return False
