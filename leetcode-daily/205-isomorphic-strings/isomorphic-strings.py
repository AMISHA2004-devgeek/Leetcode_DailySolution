class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        eles,elet={},{}
        for c1,c2 in zip(s,t):
            if ((c1 in eles and eles[c1]!=c2) or (c2 in elet and elet[c2]!=c1)):
                return False
            eles[c1]=c2
            elet[c2]=c1
        return True
        