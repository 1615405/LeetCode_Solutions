class Solution:
    # 在类加载时就初始化质数哈希表
    hashtable = [False] * 40
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    for prime in primes:
        hashtable[prime] = True

    def countPrimeSetBits(self, left: int, right: int) -> int:
        return sum(1 for x in range(left, right + 1) if self.hashtable[bin(x).count('1')])