class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        k=defaultdict(int)
        for num in nums:
            k[num]+=1
        for key, val in k.items():
            if val>n/2:
                return key
        