class Solution:
    def numSquares(self, n: int) -> int:
        # 计算可能的最大平方数
        max_square = int(n**0.5)
        squares = [i**2 for i in range(1, max_square + 1)]
        
        # 初始化dp数组
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        # 动态规划求解
        for square in squares:
            for i in range(square, n + 1):
                if i >= square:
                    dp[i] = min(dp[i], dp[i - square] + 1)
        
        return dp[n]