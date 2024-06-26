class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        from datetime import datetime
        # 将字符串格式的日期转换为 datetime 对象
        date1 = datetime.strptime(date1, "%Y-%m-%d")
        date2 = datetime.strptime(date2, "%Y-%m-%d")
    
        # 计算两个日期之间的差值，并获取天数
        delta = date2 - date1
        return abs(delta.days)  # 返回天数的绝对值以处理任意日期顺序
