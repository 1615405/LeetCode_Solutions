class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        from collections import Counter
        count1 = Counter(s1.split())
        count2 = Counter(s2.split())

        uncommon = []
        for word in count1:
            if count1[word] == 1 and word not in count2:
                uncommon.append(word)
        
        for word in count2:
            if count2[word] == 1 and word not in count1:
                uncommon.append(word)
        
        return uncommon