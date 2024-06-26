class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        seen = set(jewels)
        return sum(stone in seen for stone in stones)