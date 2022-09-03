class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:] = [elem for elem in nums if elem != val]
        return len(nums)
