class Solution:
    def numberOfSteps(self, num: int) -> int:
        c = 0
        while num:
            if num % 2:
                num = num - 1
                c += 1
            else:
                num /= 2
                c += 1
        return c
