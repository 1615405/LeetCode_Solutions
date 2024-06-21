class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def foo(s: str) -> int:
            from string import ascii_lowercase
            from collections import Counter
            cnt = Counter(s)
            return next(cnt[c] for c in ascii_lowercase if cnt[c])
        
        n = len(words)
        nums = sorted(foo(word) for word in words)

        import bisect
        return [n - bisect.bisect_right(nums, foo(q)) for q in queries]