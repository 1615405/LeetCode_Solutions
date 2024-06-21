class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num
        while left < right:
            pivot = (left + right + 1) // 2
            if pivot ** 2 <= num:   # 左边的元素都满足条件，染红色，查找红色的右边界
                left = pivot
            else:
                right = pivot - 1
        
        return left ** 2 == num