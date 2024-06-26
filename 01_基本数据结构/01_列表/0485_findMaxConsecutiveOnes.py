class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = count = 0
        for index, num in enumerate(nums):
            if num == 1:
                count += 1
                ans = max(ans, count)
            else:
                count = 0
        
        return ans