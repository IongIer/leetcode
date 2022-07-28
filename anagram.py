#bool for comparing if two strings are angrams
from collections import Counter

#my one liner that's not too efficient
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return sorted(s) == sorted(t)


#my first optimisation that makes it 50% faster than other p3 solutions
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         return sorted(s) == sorted(t)

#Solution after optimizations
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s = Counter(s)
        count_t = Counter(t)
        return count_s == count_t
