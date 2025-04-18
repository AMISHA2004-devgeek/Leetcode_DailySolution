class Solution:
    def isPalindrome(self, x: int) -> bool:
        k=str(x)
        i=0
        j=len(k)-1
        while i<j:
            if k[i]!=k[j]:
                return False
            i+=1
            j-=1
        return True