class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def hammingWeight(x: int) -> int:
            ret = 0
            while x:
                ret += 1
                x = x & (x - 1)
            return ret
        
        return sorted(arr, key=lambda x: (hammingWeight(x), x))