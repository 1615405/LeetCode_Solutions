class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # 使用sorted函数对原始列表进行排序
        sorted_heights = sorted(heights)
        
        # 使用列表推导计算排序后与原始列表中不同位置的元素数量
        mismatch_count = sum(original != sorted_height for original, sorted_height in zip(heights, sorted_heights))
        
        return mismatch_count