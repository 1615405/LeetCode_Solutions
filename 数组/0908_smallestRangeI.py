class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        max_dis = max(nums) - min(nums)
        return 0 if max_dis <= 2 * k else abs(max_dis - 2 * k)