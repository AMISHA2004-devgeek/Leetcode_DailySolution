class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res=set()
        for i in range(1,len(nums)+1):
            res.add(i)
        
        s=set(nums)
        return list(res-s)        