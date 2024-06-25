class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            pivot = (left + right + 1) // 2
            if pivot * (pivot + 1) <= 2 * n:
                left = pivot
            else:
                right = pivot - 1
        
        return left