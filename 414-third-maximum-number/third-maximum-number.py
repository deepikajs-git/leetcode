class Solution(object):
    def thirdMax(self, nums):
       
        numss=list(set(nums))
        num=sorted(numss)
        
        if len(num)>=3:
            return(num[-3])  
        else:
            return(num[-1])    

            
        