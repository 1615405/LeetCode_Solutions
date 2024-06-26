class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        from collections import Counter
        ans = 0
        cnt = Counter(chars)
        for word in words:
            c = Counter(word)
            if all(c[i] <= cnt[i] for i in c):
                ans += len(word)
        
        return ans