from collections import deque


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        if length == 0 or length == 1:
            return length
        seen = deque()
        unique = set()
        curr = 0
        best = 0
        for v in s:
            if v in unique:
                best = max(best, curr)
                while seen:
                    rem = seen.popleft()
                    unique.remove(rem)
                    if rem == v:
                        break
                seen.append(v)
                unique.add(v)
                curr = len(seen)
                
            else:
                unique.add(v)
                seen.append(v)
                curr = len(seen)
                best = max(curr, best)
        return max(best, curr)