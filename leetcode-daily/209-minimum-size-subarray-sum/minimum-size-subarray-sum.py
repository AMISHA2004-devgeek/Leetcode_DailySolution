class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        currsum=0
        maxlen=float('inf')
        for r in range(len(nums)):
            currsum+=nums[r]
            while currsum>=target:
                w=r-l+1
                maxlen=min(maxlen,w)
                currsum-=nums[l]
                l+=1
        return maxlen if maxlen < float('inf') else 0

        