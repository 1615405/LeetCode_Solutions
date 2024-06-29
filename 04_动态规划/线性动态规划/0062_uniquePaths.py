class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        f = [[1] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == 1:
                    f[i][j] = f[i][j - 1]
                elif j == 1:
                    f[i][j] = f[i - 1][j]
                else:
                    f[i][j] = f[i - 1][j] + f[i][j - 1]
        
        return f[m][n]