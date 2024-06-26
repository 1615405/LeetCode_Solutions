class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        for i in range(0, 32):
            a = (x >> i) & 1
            b = (y >> i) & 1
            count += a ^ b
        return count