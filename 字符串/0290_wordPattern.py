class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        s2t, t2s = {}, {}
        for a, b in zip(pattern, words):
            if s2t.get(a, b) != b or t2s.get(b, a) != a:
                return False
            s2t[a] = b
            t2s[b] = a
        
        return True