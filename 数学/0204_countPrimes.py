MX = 5000000
is_prime = [1] * MX
is_prime[0] = is_prime[1] = 0

for i in range(2, MX):
    if is_prime[i]:
        for j in range(i * i, MX, i):
            is_prime[j] = 0

class Solution:
    def countPrimes(self, n: int) -> int:
        return sum(is_prime[:n])