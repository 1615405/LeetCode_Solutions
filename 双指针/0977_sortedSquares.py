class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right, pos = 0, n - 1, n - 1
        ans = [0] * n

        while left <= right:
            if nums[left] ** 2 <= nums[right] ** 2:
                ans[pos] = nums[right] ** 2
                right -= 1
            else:
                ans[pos] = nums[left] ** 2
                left += 1
            pos -= 1
        
        return ans