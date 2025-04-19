from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count=[0]*26
        for ch in s:
            count[ord(ch)-ord('a')]+=1
        for r in t:
            count[ord(r)-ord('a')]-=1
        return count==[0]*26



        