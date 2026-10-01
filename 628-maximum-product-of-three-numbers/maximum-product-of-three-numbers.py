class Solution(object):
    def maximumProduct(self, nums):
        a = sorted(nums)
        num = max(a[-1]*a[-2]*a[-3],a[0]*a[1]*a[-1])
        return num
        