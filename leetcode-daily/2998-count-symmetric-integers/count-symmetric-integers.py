class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        c=0
        for i in range(low,high+1):
            s=str(i)
            if len(s)%2==0:
                mid=len(s)//2
                if sum(int(x) for x in s[:mid])==sum(int(x) for x in s[mid:]):
                    c+=1
        return c

        