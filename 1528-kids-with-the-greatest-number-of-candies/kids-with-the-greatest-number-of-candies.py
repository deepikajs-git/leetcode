class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maximum = max(candies)
        return [c + extraCandies >= maximum for c in candies]
        
        