class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l=0
        elecount=0
        maxlen=0
        for r in range(len(nums)):
            if nums[r]==0:
                elecount+=1
            if elecount>1:
                if nums[l]==0:
                    elecount-=1
                l+=1
            maxlen=max(maxlen,r-l+1)
        return maxlen-1

        