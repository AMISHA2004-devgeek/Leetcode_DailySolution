from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l=0
        k=[]
        pcount=Counter(p)
        angcount=Counter()
        for r in range(len(s)):
            angcount[s[r]]+=1
            while r-l+1 > len(p):
                angcount[s[l]]-=1
                if angcount[s[l]]==0:
                    del angcount[s[l]]
                l += 1
            if angcount==pcount:
                k.append(l)
        return k


        