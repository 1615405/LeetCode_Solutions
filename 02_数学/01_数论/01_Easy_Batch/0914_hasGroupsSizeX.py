class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        from collections import Counter
        from functools import reduce
        
        count = Counter(deck)
        # 使用 reduce 函数和 gcd 函数计算所有频率的最大公约数
        gcd_value = reduce(math.gcd, count.values())
        # 如果最大公约数至少为 2，则可以分组
        return gcd_value >= 2