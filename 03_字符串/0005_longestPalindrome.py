class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandAroundCenter(left, right) -> tuple:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = expandAroundCenter(i, i)
            left2, right2 = expandAroundCenter(i, i + 1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
    
        return s[start: end + 1]