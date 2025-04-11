class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        k = {}
        for num in nums:
            k[num] = k.get(num,0) + 1

        for key in k:
            if k[key] == 1:
                return key
