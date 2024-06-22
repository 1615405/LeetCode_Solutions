class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        sign = 0
        while i < len(bits):
            if bits[i] == 0:
                i += 1
                sign = 1
            elif bits[i] == 1:
                i += 2
                sign = 2

        return True if sign == 1 else False