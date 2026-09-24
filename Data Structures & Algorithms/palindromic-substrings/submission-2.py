class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for i in range(n)]
        sol = 0
        for i in range(n-1, -1, -1):
            for j in range(n):
                if i == j:
                    dp[i][j] = True
                elif j - i == 1 and s[i] == s[j]:
                    dp[i][j] = True
                elif i < len(s) - 1 and j > 0 and dp[i+1][j-1]:
                    if s[i] == s[j]:
                        dp[i][j] = True

                if dp[i][j]:
                    sol += 1
        return sol