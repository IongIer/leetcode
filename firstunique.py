from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        char = Counter(s)
        for c in char:
            if char[c] == 1:
                return s.index(c)
        return -1
