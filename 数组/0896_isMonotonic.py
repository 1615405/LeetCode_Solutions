class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        from itertools import pairwise
        inc = dec = True
        for a, b in pairwise(nums):
            if a < b:
                dec = False
            if a > b:
                inc = False
            if not inc and not dec:
                return False
        
        return True