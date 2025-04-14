class Solution:
    def countBits(self, n: int) -> List[int]:
        k=[0]*(n+1)
        for i in range(n+1):
            k[i]=k[i>>1]+(i&1)
        return k




        