class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        window_sum=sum(nums[:k])
        maxsum=window_sum

        for i in range(k,n):
            window_sum +=nums[i]-nums[i-k]
            maxsum=max(maxsum,window_sum)

        return maxsum/k


        