class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = 0
        for col in zip(*strs):
            if len(set(col)) > 1:
                break
            lcp += 1
        
        return strs[0][:lcp]