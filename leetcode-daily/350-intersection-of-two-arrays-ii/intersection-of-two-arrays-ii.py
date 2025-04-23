from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        k=Counter(nums1)
        for x in nums2:
            if k[x]>0:
                res.append(x)
                k[x]-=1
        return res