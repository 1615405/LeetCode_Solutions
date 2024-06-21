class Solution:
    def myPow(self, base: float, exponent: int) -> float:
        def power(base, exponent):
            if exponent == 0:
                return 1
            ans = 1
            while exponent:
                if exponent & 1:
                    ans = ans * base
                exponent >>= 1
                base = base * base
            return ans

        if exponent < 0:
            base = 1 / base
            exponent = -exponent
        
        return power(base, exponent)