class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = [0] * 102
        for num in nums:
            count[num + 1] += 1  # 使用偏移1的技巧简化计算

        # 累加计数数组，使得count[i]表示小于i的元素数量
        for i in range(1, 102):
            count[i] += count[i - 1]

        # 根据计数数组构建结果
        return [count[num] for num in nums]