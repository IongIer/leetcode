from collections import defaultdict


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        def make_new_pattern(pattern):
            count_pattern = 0
            in_pattern = defaultdict()
            new_pattern = []
            for char in pattern:
                if char in in_pattern:
                    new_pattern.append(in_pattern[char])
                else:
                    count_pattern += 1
                    in_pattern[char] = count_pattern
                    new_pattern.append(in_pattern[char])
            return new_pattern

        return make_new_pattern(pattern) == make_new_pattern(s.split(" "))
