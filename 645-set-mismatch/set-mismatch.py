class Solution(object):
    def findErrorNums(self, nums):
        a = 0
        b = 0
        num = nums[:]
        num = list(set(num))
        for i in range(1,len(nums)+1):
            if i not in nums:
                a = i
                break
        for i in num:
            if nums.count(i)==2:
                b = i
                break
        return [b,a]        