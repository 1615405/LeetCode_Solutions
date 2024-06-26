class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        def get(x: int) -> str:
            if x % 15 == 0:
                return "FizzBuzz"
            elif x % 3 == 0:
                return "Fizz"
            elif x % 5 == 0:
                return "Buzz"
            return str(x)
        
        return [get(x) for x in range(1, n + 1)]