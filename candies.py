class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        top_kid =  max(candies)
        return [i + extraCandies >= top_kid for i in candies]