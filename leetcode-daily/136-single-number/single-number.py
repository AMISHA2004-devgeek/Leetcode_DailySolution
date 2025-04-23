class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        k=Counter(nums)
        for k ,v in k.items():
            if v==1:
                return k 
        