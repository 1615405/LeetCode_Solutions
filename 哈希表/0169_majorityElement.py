class Solution:
    def majorityElement(self, nums):
        # 初始阶段：候选人为空，计数器为0
        candidate = None
        count = 0

        # 第一阶段：找到可能的多数元素
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        # 第二阶段：验证候选人是否为多数元素
        count = 0
        for num in nums:
            if num == candidate:
                count += 1
        
        if count > len(nums) // 2:
            return candidate
        else:
            raise ValueError("No majority element found")