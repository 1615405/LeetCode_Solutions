class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        while left < right:
            pivot = (left + right) // 2
            if letters[pivot] > target:
                right = pivot
            else:
                left = pivot + 1

        if letters[left] <= target:
            return letters[0]
        return letters[left]