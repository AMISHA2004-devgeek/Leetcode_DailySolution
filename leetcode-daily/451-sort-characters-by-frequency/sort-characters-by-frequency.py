class Solution:
    def frequencySort(self, s: str) -> str:
        k=defaultdict(int)
        for char in s:
            k[char]+=1

        dictsort=sorted(k.items(),key=lambda x: x[1], reverse=True)
        res=''
        for char,freq in dictsort:
            res+=char*freq

        return res


        