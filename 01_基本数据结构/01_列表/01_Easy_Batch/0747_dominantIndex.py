class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_index = 0
        max_value = nums[0]
        second_max = -float('inf')

        for i in range(1, len(nums)):
            if nums[i] > max_value:
                second_max = max_value
                max_value = nums[i]
                max_index = i
            elif nums[i] > second_max:
                second_max = nums[i]
        
        return max_index if max_value >= 2 * second_max else -1
