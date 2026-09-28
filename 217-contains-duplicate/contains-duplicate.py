class Solution(object):
    def containsDuplicate(self, nums):
        nums.sort()
        return len(nums) != len(set(nums))
        