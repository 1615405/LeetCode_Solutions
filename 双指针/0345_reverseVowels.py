class Solution:
    def reverseVowels(self, s: str) -> str:
        def isVowel(ch: str) -> bool:
            return ch in "aeiouAEIOU"
        
        left, right = 0, len(s) - 1
        slist = list(s)
        while left < right:
            while left < right and not isVowel(s[left]):
                left += 1
            while left < right and not isVowel(s[right]):
                right -= 1
            if left < right:
                slist[left], slist[right] = slist[right], slist[left]
            left += 1
            right -= 1
        
        return ''.join(slist)