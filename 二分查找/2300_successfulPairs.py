class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ans = []
        potions.sort()
        for spell in spells:
            left, right = 0, len(potions) - 1
            while left < right:
                pivot = (left + right) // 2
                if potions[pivot] * spell >= success:
                    right = pivot
                else:
                    left = pivot + 1
            print(left)
            if spell * potions[left] < success:
                ans.append(0)
            else:
                count = len(potions) - left
                ans.append(count)
        
        return ans