from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for x in range(len(strs[0])):
            new_word = [word[x] for word in strs]
            if new_word != sorted(new_word):
                count += 1
                
        return count
            
