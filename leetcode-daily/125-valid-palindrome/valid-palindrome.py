class Solution:
    def isPalindrome(self, s: str) -> bool:
        r=''.join(s).lower()
        k=""
        for ch in r:
            if ch.isalnum():
                k+=ch
        return k==k[::-1]
        

        