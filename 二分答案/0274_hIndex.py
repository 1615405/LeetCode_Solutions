class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left, right = 0, len(citations)
        while left < right:
            pivot = (left + right + 1) // 2
            count = 0
            for cite in citations:
                count += cite >= pivot
            if pivot <= count:
                left = pivot
            else:
                right = pivot - 1
        
        return left