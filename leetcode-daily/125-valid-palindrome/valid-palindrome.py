class Solution:
    def isPalindrome(self, s: str) -> bool:
        r=s.lower()
        i=0
        j=len(r)-1
        while i<j:
            if not r[i].isalnum():
                i+=1
                continue
            if not r[j].isalnum():
                j-=1
                continue
            if r[i]!=r[j]:
                return False
            else:
                i+=1
                j-=1
        return True
       
                
        

        