class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        res=""
        for x in s:
            if x.isalnum():
                res+=x.lower()
        i=0
        j=len(res)-1
        while i<j:
            if res[i]!=res[j]:
                return False
            i+=1
            j-=1
        return True
            


