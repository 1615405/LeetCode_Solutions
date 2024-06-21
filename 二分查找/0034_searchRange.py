class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums == []:
            return [-1, -1]

        left, right = 0, len(nums) - 1
        while left < right:
            pivot = (left + right) // 2
            if nums[pivot] >= target:
                right = pivot
            else:
                left = pivot + 1
        
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r + 1) // 2
            if nums[mid] <= target:
                l = mid
            else:
                r = mid - 1
        
        if nums[left] != target:
            return [-1, -1]
        return [left, l]