class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left, right = 1, len(nums) - 1
        while left < right:
            cnt = 0
            pivot = (left + right) // 2
            for num in nums:
                cnt += (num <= pivot)
            if cnt <= pivot:
                left = pivot + 1
            else:
                right = pivot
        
        return left