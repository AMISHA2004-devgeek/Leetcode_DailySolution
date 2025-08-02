from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq=Counter(nums)
        for c in freq.values():
            if c>1:
                return True
        return False
        