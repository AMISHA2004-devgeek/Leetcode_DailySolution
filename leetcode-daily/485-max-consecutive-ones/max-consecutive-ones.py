class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxc=c=0
        for i in range(len(nums)):
            if nums[i]==1:
                c+=1
                maxc=max(maxc,c)
            else:  
                c=0
        return maxc


        