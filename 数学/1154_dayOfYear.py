class Solution: 
    def dayOfYear(self, date: str) -> int:
        from datetime import datetime
        date_object = datetime.strptime(date, "%Y-%m-%d")
        return date_object.timetuple().tm_yday