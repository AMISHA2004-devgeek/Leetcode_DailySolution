class Solution(object):
    def findDifferentBinaryString(self, nums):
        res=[]
        for i in range(0,len(nums)):
            if nums[i][i]=='0':
                res.append('1')
            else:
                res.append('0')
        k="".join(res)
        return k
        