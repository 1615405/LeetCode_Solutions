class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t, t2s = {}, {}

        for a, b in zip(s, t):
            if s2t.get(a, b) != b or t2s.get(b, a) != a:
                return False
            s2t[a], t2s[b] = b, a

        return True