class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # 移除破折号，并转换为大写
        s = s.replace("-", "").upper()
        # 初始化结果字符串和第一段的长度
        result = []
        first_group_length = len(s) % k or k  # 如果 len(s) % k 为 0，则取 k

        # 添加第一组
        result.append(s[:first_group_length])

        # 每 k 个字符形成一组，添加到结果列表中
        for i in range(first_group_length, len(s), k):
            result.append(s[i:i + k])

        # 使用破折号连接所有组并返回
        return "-".join(result)