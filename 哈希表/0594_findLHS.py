class Solution:
    def findLHS(self, nums: List[int]) -> int:
        from collections import Counter
        cnt = Counter(nums)

        max_seq = 0
        for k in cnt:
            if cnt[k - 1] > 0:
                max_seq = max(max_seq, cnt[k - 1] + cnt[k])
            if cnt[k + 1] > 0:
                max_seq = max(max_seq, cnt[k + 1] + cnt[k])
        
        return max_seq