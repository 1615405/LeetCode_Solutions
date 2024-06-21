class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        counts = Counter(s)
        length = 0
        has_odd = False

        for count in counts.values():
            # 增加的长度是当前字符出现次数的最大偶数部分
            length += (count // 2) * 2
            # 检查是否存在奇数次字符，如果有，设置 has_odd 为 True
            if count % 2 == 1:
                has_odd = True
        
        # 如果存在奇数次字符，最长回文长度可以额外增加1
        return length + (1 if has_odd else 0)