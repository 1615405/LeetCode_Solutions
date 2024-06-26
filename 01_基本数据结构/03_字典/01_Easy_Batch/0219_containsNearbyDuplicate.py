class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashtable = dict()
        for index, num in enumerate(nums):
            if num in hashtable:
                if index - hashtable[num] <= k:
                    return True
            hashtable[num] = index
        
        return False