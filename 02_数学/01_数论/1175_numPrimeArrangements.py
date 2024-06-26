class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def is_prime(n: int) -> bool:
            if n < 2:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            limit = int(n**0.5) + 1
            for i in range(3, limit, 2):
                if n % i == 0:
                    return False
            return True

        # 计算1到n之间有多少个素数
        cnt = sum(1 for i in range(1, n + 1) if is_prime(i))

        # 预计算阶乘并取模，使用整数进行所有操作
        mod = 1000000007
        factor = [1] * (n + 1)
        for i in range(2, n + 1):
            factor[i] = factor[i - 1] * i % mod
        
        # 根据素数的数量和非素数的数量计算排列，并取模
        return (factor[cnt] * factor[n - cnt]) % mod