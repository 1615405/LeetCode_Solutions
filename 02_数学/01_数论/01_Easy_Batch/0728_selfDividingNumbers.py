class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def isSelfDividing(num):
            original = num
            while num:
                digit = num % 10
                # 如果数字中有0，或者原始数不能被其某一位整除，则不是自除数
                if digit == 0 or original % digit != 0:
                    return False
                num //= 10
            return True
        
        return [i for i in range(left, right + 1) if isSelfDividing(i)]