class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        left = 0
        char_set = set()

        for right, char in enumerate(s):
            # 如果字符已在集合中，移除窗口左侧的字符直到该字符可以被添加进集合
            while char in char_set:
                char_set.remove(s[left])
                left += 1
            # 将当前字符添加到集合中
            char_set.add(char)
            # 更新最大长度
            max_length = max(max_length, right - left + 1)

        return max_length