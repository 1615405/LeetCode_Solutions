class Solution:
    def judgeCircle(self, moves: str) -> bool:
        from collections import Counter
        counter = Counter(moves)

        return counter['U'] == counter['D'] and counter['L'] == counter['R']
