class Solution(object):
    def merge(self, nums1, m, nums2, n):
        while 0<n:
            nums1.remove(0)
            n-=1
        for i in nums2:
            nums1.append(i)
        nums1.sort()    

        