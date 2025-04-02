class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count=[0]*26
        for char in s:
            count[ord(char)-ord('a')]+=1
        for x in t:
            count[ord(x)-ord('a')]-=1

        return count==[0]*26
            


        