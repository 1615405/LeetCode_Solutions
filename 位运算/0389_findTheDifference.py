class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0  # 初始化结果为 0
        for char in s:
            result ^= ord(char)  # XOR 字符串 s 的字符
        for char in t:
            result ^= ord(char)  # XOR 字符串 t 的字符
        
        return chr(result)  # 将最终的结果转换回字符