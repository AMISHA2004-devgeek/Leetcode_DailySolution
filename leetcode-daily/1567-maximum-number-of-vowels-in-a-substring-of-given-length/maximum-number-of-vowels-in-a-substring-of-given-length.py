class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vow="aeiou"
        l=0
        c=0
        maxc=0
        for r in range(len(s)):
            if s[r] in vow:
                c+=1
            while r-l+1 >k:
                if s[l] in vow:
                    c-=1
                l+=1
            maxc = max(maxc, c)
        return maxc

