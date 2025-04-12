from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counts = [0, 0, 0]
        for num in nums:
            counts[num] += 1
        
        zeroes, ones, twos = counts
        nums[:zeroes] = [0] * zeroes
        nums[zeroes : zeroes + ones] = [1] * ones
        nums[zeroes + ones : zeroes + ones + twos] = [2] * twos
