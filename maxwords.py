class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maximum = 0
        for s in sentences:
            maximum = max(maximum, len(s.split()))
        return maximum
