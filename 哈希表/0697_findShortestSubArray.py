class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        from collections import Counter
        first, last = {}, {}
        count = Counter(nums)

        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i
            last[num] = i
        
        degree = max(count.values())
        min_length = len(nums)  # 初始值设置为 nums 的长度
        
        for num, cnt in count.items():
            if cnt == degree:
                min_length = min(min_length, last[num] - first[num] + 1)

        return min_length