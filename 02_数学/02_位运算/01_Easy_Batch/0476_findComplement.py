class Solution:
    def findComplement(self, num: int) -> int:
        highbit = num.bit_length()
        mask = (1 << (highbit)) - 1
        return num ^ mask