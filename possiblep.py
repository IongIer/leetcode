class Solution:
    def isPalindrome(self, s: str) -> bool:
        possible_palindrome = [c.lower() for c in s if c.isalnum()]
        length = len(possible_palindrome)
        for i in range(length // 2):
            if possible_palindrome[i] != possible_palindrome[~i]:
                return False
        return True 