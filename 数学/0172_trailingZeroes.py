class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n:
            count += n // 5
            n //= 5
        return count