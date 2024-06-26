class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single_xor = 0
        for num in nums:
            single_xor ^= num
        return single_xor