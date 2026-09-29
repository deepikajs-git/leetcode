class Solution(object):
    def findTheDifference(self, s, t):
        for x in t:
            if t.count(x)!=s.count(x):
                return x
        