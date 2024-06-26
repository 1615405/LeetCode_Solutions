class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        from collections import Counter
        counter = collections.Counter(arr)
        for n in arr:
            if n != 0 and counter[2 * n] >= 1:
                return True
            if n == 0 and counter[2 * n] >= 2:
                return True
        return False
