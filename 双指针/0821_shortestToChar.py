class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        ans = [float('inf')] * n  # 初始化答案数组为无穷大
        
        # 从左到右遍历，记录每个位置与左侧最近的c的距离
        prev = float('-inf')  # 使用-inf表示还未遇到字符c
        for i in range(n):
            if s[i] == c:
                prev = i
            ans[i] = min(ans[i], i - prev)
        
        # 从右到左遍历，记录每个位置与右侧最近的c的距离
        prev = float('inf')  # 使用inf表示还未遇到字符c
        for i in range(n-1, -1, -1):
            if s[i] == c:
                prev = i
            ans[i] = min(ans[i], prev - i)
        
        return ans