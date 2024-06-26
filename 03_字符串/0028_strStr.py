class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 如果 needle 为空字符串，返回0
        if not needle:
            return 0
        
        # 如果 needle 长度大于 haystack，直接返回 -1
        if len(needle) > len(haystack):
            return -1
        
        # 定义哈希函数
        def hash_function(s):
            import hashlib
            return hashlib.md5(s.encode()).hexdigest()
        
        # 计算 needle 的哈希值
        needle_hash = hash_function(needle)
        
        # 滑动窗口匹配
        for i in range(len(haystack) - len(needle) + 1):
            current_window = haystack[i:i+len(needle)]
            window_hash = hash_function(current_window)
            
            if window_hash == needle_hash:
                return i
        
        return -1