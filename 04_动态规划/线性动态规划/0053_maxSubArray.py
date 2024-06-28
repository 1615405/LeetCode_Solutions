class Solution:
    def maxSubArray1(self, nums: List[int]) -> int:
        current_max = global_max = nums[0]

        for num in nums[1:]:
            current_max = max(num, current_max + num)
            global_max = max(global_max, current_max)
        
        return global_max
    
    
    def maxSubArray2(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-float('inf')] * n
        dp[0] = nums[0]
        
        for i in range(1, n):
            # 状态转移方程
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        
        return max(dp)