class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        from collections import Counter
        import string
        
        # 将所有字符转为小写并替换标点为空格
        normalized_str = paragraph.lower()
        for c in string.punctuation:
            normalized_str = normalized_str.replace(c, ' ')
        
        # 统计每个单词出现的次数
        words = normalized_str.split()
        counter = Counter(words)
        
        # 移除禁用词汇
        for ban in banned:
            del counter[ban]
        
        # 返回出现次数最多的单词
        return counter.most_common(1)[0][0]
