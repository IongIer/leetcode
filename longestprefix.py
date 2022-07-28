# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        max_len = len(min(strs, key=len))
        while max_len > 0:
            possible_s = {element[:max_len] for element in strs}
            if len(possible_s) == 1:
                return list(possible_s)[0]
            max_len -= 1
        return ""
