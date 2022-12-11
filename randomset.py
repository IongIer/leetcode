class RandomizedSet:
    def __init__(self):
        self.arr = []
        self.hash = {}

    def insert(self, val: int) -> bool:
        if val in self.hash:
            return False
        self.hash[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hash:
            return False
        self.hash[self.arr[-1]] = self.hash[val]
        self.arr[self.hash[val]] = self.arr[-1]
        self.arr[-1] = val
        self.hash.pop(val)
        self.arr.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)
