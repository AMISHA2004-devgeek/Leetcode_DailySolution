class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sumc=maxsum=nums[0]
        for i in range(1,len(nums)):
            sumc=max(nums[i],nums[i]+sumc)
            maxsum=max(sumc,maxsum)
        return max(maxsum,sumc)

        