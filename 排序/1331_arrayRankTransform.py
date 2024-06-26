class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_unique = sorted(set(arr))
        rank_num = {value: idx + 1 for idx, value in enumerate(sorted_unique)}

        return [rank_num[num] for num in arr]
