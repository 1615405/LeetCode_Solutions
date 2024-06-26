class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        xor_sum = 0

        # 计算1到n所有数字和nums中所有数字的异或结果
        for i in range(1, n + 1):
            xor_sum ^= i
        for num in nums:
            xor_sum ^= num

        # 取得xor_sum中最低的1位
        lowbit = xor_sum & (-xor_sum)
        type1, type2 = 0, 0

        # 根据lowbit将数字分类并进行异或
        for i in range(1, n + 1):
            if i & lowbit:
                type2 ^= i
            else:
                type1 ^= i
        for num in nums:
            if num & lowbit:
                type2 ^= num
            else:
                type1 ^= num

        # 检查type1是否在nums中，以确定重复的数字
        return [type1, type2] if type1 in nums else [type2, type1]