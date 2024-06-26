class Solution:
    def reverseBits(self, n: int) -> int:
        M1 = 0x55555555  # 01010101010101010101010101010101
        M2 = 0x33333333  # 00110011001100110011001100110011
        M4 = 0x0f0f0f0f  # 00001111000011110000111100001111
        M8 = 0x00ff00ff  # 00000000111111110000000011111111

        # Swap odd and even bits
        n = (n >> 1 & M1) | ((n & M1) << 1)
        
        # Swap consecutive pairs
        n = (n >> 2 & M2) | ((n & M2) << 2)
        
        # Swap nibbles ...
        n = (n >> 4 & M4) | ((n & M4) << 4)
        
        # Swap bytes
        n = (n >> 8 & M8) | ((n & M8) << 8)
        
        # Swap 2-byte long pairs
        n = (n >> 16) | (n << 16) & 0xFFFFFFFF  # Ensure n is treated as 32 bits

        return n