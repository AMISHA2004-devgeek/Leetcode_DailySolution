class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currsum=0
        c=0
        ps=defaultdict(int)
        ps[0]=1
        for r in range(len(nums)):
            currsum+=nums[r]
            c+=ps[currsum-k]
            ps[currsum]+=1
        return c
        