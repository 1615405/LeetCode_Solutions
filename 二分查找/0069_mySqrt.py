class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left < right:
            pivot = (left + right + 1) // 2
            if pivot ** 2 <= x:
                left = pivot
            else:
                right = pivot - 1
        
        return left