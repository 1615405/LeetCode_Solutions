class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor_sum = 0
        for i in range(0, len(nums) + 1):
            xor_sum ^= i
        
        for num in nums:
            xor_sum ^= num
        
        return xor_sum