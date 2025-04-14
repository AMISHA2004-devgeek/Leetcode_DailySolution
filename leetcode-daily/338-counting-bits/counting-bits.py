class Solution:
    def countBits(self, n: int) -> List[int]:
        k=[0]*(n+1)
        for i in range(n+1):
            k[i]=bin(i).count('1')
        return k




        