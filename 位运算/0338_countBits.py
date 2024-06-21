class Solution:
    def countBits(self, n: int) -> List[int]:
        def hammingWeight(n: int) -> int:
            ret = 0
            while n:
                ret += 1
                n = n & (n - 1)
            return ret
        
        bits = [hammingWeight(i) for i in range(n + 1)]
        return bits