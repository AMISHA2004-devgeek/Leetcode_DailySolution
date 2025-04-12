class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d=defaultdict(int)
        end=[]
        for num in arr1:
            if num not in arr2:
                end.append(num)
            d[num]+=1

        end.sort()
        res=[]
        for n in arr2:
            for _ in range(d[n]):
                res.append(n)

        return res+end


