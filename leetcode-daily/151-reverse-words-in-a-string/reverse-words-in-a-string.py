class Solution:
    def reverseWords(self, s: str) -> str:
        k=s.strip().split()
        r=" ".join(k[::-1])
        return r

        