class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        c=[0]*26
        maxele=0
        maxlen=0
        for r in range(len(s)):
            c[ord(s[r])-ord('A')]+=1
            maxele=max(maxele,c[ord(s[r])-ord('A')])
            while (r-l+1)-maxele >k:
                c[ord(s[l])-ord('A')]-=1
                l+=1
            maxlen=max(maxlen,r-l+1)
        return maxlen


            
       