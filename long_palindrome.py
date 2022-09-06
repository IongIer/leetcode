from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        evens = sum([counts[elem] for elem in counts if counts[elem] % 2 == 0])
        odds = [counts[elem] for elem in counts if counts[elem] % 2]
        sum_odds = sum(odds) - len(odds) + 1
        return evens + sum_odds if odds else evens
