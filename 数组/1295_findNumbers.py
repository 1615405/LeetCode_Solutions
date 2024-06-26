class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        cnt = 0
        for num in nums:
            str_num = str(num)
            if len(str_num) % 2 == 0:
                cnt += 1
        
        return cnt
