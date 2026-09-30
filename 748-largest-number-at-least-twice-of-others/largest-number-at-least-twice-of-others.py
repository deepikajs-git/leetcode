class Solution(object):
    def dominantIndex(self, nums):
        num=sorted(nums)  
        flag=True
        for i in range(len(nums)):
            if num[-1]==nums[i]:
                continue
            elif num[-1] < 2* nums[i]:
                flag=False
        if flag:
            z=nums.index(num[-1])
            return z
        else:
            return -1

        