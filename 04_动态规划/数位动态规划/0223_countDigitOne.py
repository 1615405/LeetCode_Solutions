class Solution:
    def countDigitOne1(self, n: int) -> int:
        from functools import cache
        s = str(n)
        @cache
        def f(i: int, cnt1: int, is_limit: bool) -> int:
            if i == len(s):
                return cnt1
            result = 0
            up = int(s[i]) if is_limit else 9
            for d in range(up + 1):  # 枚举要填入的数字 d
                result += f(i + 1, cnt1 + (d == 1), is_limit and d == up)
            return result
            
        return f(0, 0, True)
    
    def countDigitOne2(self, n: int) -> int:
        digit, result = 1, 0
        high, cur, low = n // 10, n % 10, 0
        while high or cur:
            if cur == 0:
                result += high * digit
            elif cur == 1:
                result += high * digit + low + 1
            else:
                result += (high + 1) * digit
            
            low += cur * digit
            cur = high % 10
            high //= 10
            digit *= 10
        
        return result