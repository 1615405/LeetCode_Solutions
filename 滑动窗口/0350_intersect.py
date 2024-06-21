class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        from collections import Counter
        cnt = Counter(nums1)

        intersection = list()
        for num in nums2:
            if (count := cnt.get(num, 0)) > 0:
                intersection.append(num)
                cnt[num] -= 1
                if cnt[num] == 0:
                    cnt.pop(num)
        
        return intersection