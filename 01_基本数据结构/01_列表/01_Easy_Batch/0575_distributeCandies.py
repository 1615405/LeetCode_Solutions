class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType)
        max_candies = n // 2
        unqiue_candies = len(set(candyType))
        return min(max_candies, unqiue_candies)