class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxcount=0
        l=0
        zeroc=0
        
        for r in range(len(nums)):
            if nums[r]==0:
                zeroc+=1
            
            while zeroc>k:
                if nums[l]==0:
                    zeroc-=1
                l+=1
            
            maxcount= max(maxcount,r-l+1)
        
        return maxcount
