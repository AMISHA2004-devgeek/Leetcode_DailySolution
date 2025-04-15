class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=set()
        k=0
        l=0
        for r in range(len(s)):
            while s[r] in res:
                res.remove(s[l])
                l+=1
            w=(r-l)+1
            k=max(k,w)
            res.add(s[r])
        return k



           
        