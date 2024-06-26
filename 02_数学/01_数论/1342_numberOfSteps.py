class Solution:
    def numberOfSteps(self, num: int) -> int:
        ret = 0
        while num:
            ret += 1
            num = num - 1 if num & 1 else num // 2
        return ret
