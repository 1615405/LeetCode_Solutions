class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # 求最小正数下标
        left, right = 0, len(nums) - 1
        while left < right:
            pivot = (left + right) // 2
            if nums[pivot] > 0:
                right = pivot
            else:
                left = pivot + 1
        
        # 求最大负数下标
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r + 1) // 2
            if nums[mid] < 0:
                l = mid
            else:
                r = mid - 1
            
        count1 = l + 1 if nums[l] < 0 else 0
        count2 = len(nums) - left if nums[left] > 0 else 0

        return max(count1, count2)