from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_ransom = Counter(ransomNote)
        count_magazine = Counter(magazine)
        return count_ransom <= count_magazine
