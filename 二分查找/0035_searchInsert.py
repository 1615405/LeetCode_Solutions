class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            pivot = (left + right + 1) // 2
            if nums[pivot] <= target:
                left = pivot
            else:
                right = pivot - 1
        
        if nums[0] > target:
            return 0
        return left if nums[left] == target else left + 1