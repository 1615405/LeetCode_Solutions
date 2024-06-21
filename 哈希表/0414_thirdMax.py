class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        from sortedcontainers import SortedList
        s = SortedList()
        for num in nums:
            if num not in s:
                s.add(num)
                if len(s) > 3:
                    s.pop(0)
        
        return s[0] if len(s) == 3 else s[-1]