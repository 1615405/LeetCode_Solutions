class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # 0xAAAAAAAA 是一个32位整数，其中偶数位置上的位都是1，奇数位置上的位都是0
        NOT_FOUR_POWER_MASK = 0xAAAAAAAA
        
        # n 必须大于 0
        if n <= 0:
            return False

        # n 必须是 2 的幂
        if n & (n - 1) != 0:
            return False

        # n 的 1 必须在 4 的幂的位置，即1的位置必须在奇数位上
        return (n & NOT_FOUR_POWER_MASK) == 0