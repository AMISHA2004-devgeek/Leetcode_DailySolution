class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        diff=0
        mindiff = float('inf') 
        for i in range(len(nums)-k+1):
            diff=nums[i+k-1]-nums[i]
            mindiff=min(diff,mindiff)
        return mindiff
        