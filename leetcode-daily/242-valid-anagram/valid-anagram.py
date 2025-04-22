class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        cnt=[0]*26
        for c in s:
            cnt[ord(c)-ord('a')]+=1
        for x in t:
            cnt[ord(x)-ord('a')]-=1
        
        return cnt==[0]*26

        