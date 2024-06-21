class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        slist = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and (not s[i].isalpha()):
                i += 1
            while i < j and (not s[j].isalpha()):
                j -= 1
            if i < j:
                slist[i], slist[j] = slist[j], slist[i]
            i, j = i + 1, j - 1
        
        return "".join(slist)