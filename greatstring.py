class Solution:
    def makeGood(self, s: str) -> str:
        def helper(s: str) -> str:
            for i, c in enumerate(s[:-1]):
                if c.lower() == s[i + 1].lower() and c != s[i + 1]:
                    return s[:i] + s[i + 2 :]
            return s

        while True:
            temp = s
            s = helper(s)
            if temp == s:
                return s
