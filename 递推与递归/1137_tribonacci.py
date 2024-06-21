class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        
        a, b, c = 0, 1, 1  # 初始化前三个 Tribonacci 数
        # 直接从第三项开始计算到第 n 项
        for i in range(3, n + 1):
            a, b, c = b, c, a + b + c  # 滚动更新三个变量
        
        return c