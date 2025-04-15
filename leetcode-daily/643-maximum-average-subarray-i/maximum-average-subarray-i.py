class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        maxsum=currsum=sum(nums[:k])
        for i in range(k,n):
            currsum=currsum+nums[i]-nums[i-k]
            maxsum=max(maxsum,currsum)
        return maxsum/k
        