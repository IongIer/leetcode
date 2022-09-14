class MinStack:
    def __init__(self):
        self.s = []
        self.minimum = []

    def push(self, val: int) -> None:
        self.s.append(val)
        if self.minimum:
            self.minimum.append(min(val, self.minimum[-1]))
        else:
            self.minimum.append(val)

    def pop(self) -> None:
        self.s.pop()
        self.minimum.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.minimum[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
