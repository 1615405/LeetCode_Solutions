class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # 判断两个字符串的拼接是否相等
        if str1 + str2 != str2 + str1:
            return ""
        
        # 求两个数的最大公因数
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        # 求两个字符串长度的最大公因数
        gcd_length = gcd(len(str1), len(str2))
        
        # 截取任意一个字符串的前 gcd_length 个字符
        return str1[:gcd_length]