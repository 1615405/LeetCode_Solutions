class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        cnt = Counter(magazine)

        for char in ransomNote:
            if cnt[char] <= 0:  # 直接检查计数是否足够
                return False
            cnt[char] -= 1
        
        return True  # 如果所有字符都能匹配，返回True