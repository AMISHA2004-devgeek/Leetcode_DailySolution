class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        k=defaultdict(int)
        for num in nums:
            k[num]+=1
        for key , val in k.items():
            if val==1:
                return key
        