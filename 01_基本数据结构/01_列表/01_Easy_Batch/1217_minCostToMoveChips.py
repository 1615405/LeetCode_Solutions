class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd = sum(1 for num in position if num % 2 == 1)
        even = sum(1 for num in position if num % 2 == 0)
        return min(odd, even)