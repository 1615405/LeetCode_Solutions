class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        xor_n = n ^ (n >> 1)

        return xor_n & (xor_n + 1) == 0