class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        from collections import Counter
        common_count = Counter(words[0])

        for word in words[1:]:
            current_count = Counter(word)
            common_count &= current_count
        
        result = []
        for char, cnt in common_count.items():
            result.extend([char] * cnt)
        
        return result