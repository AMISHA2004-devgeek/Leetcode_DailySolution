class Solution:
    def frequencySort(self, s: str) -> str:
        k=defaultdict(int)
        for char in s:
            k[char]+=1

        dictsort=sorted(k.items(),key=lambda x: x[1], reverse=True)
        res=''
        for key,val in dictsort:
            for _ in range(val):
                res+=key

        return res


        