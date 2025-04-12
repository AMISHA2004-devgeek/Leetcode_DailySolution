class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d=defaultdict(int)
        k=set(arr2)
        end=[]
        for num in arr1:
            if num not in k:
                end.append(num)
            d[num]+=1

        end.sort()
        res=[]
        for n in arr2:
            for _ in range(d[n]):
                res.append(n)

        return res+end


