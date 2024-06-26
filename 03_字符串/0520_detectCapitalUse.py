class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # 检查全部字母是否都是大写
        if word.upper() == word:
            return True
        # 检查所有字母是否都不是大写
        if word.lower() == word:
            return True
        # 检查仅首字母大写的情况，确保只有第一个字符大写，且长度超过1
        if word[0].upper() == word[0] and word[1:].lower() == word[1:]:
            return True
        # 如果上述条件都不符合，则返回False
        return False