class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for i in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(n):
                if i == j:
                    dp[i][j] = True
                elif j - i == 1:
                    if s[i] == s[j]:
                        dp[i][j] = True
                elif i < n-1 and j != 0 and dp[i+1][j-1]:
                    if s[i] == s[j]:
                        dp[i][j] = True
        m_len = 0
        res = ''
        for i in range(n):
            for j in range(n):
                if dp[i][j]:
                    if m_len < j - i + 1:
                        m_len = j - i + 1
                        res = s[i:j+1]
        return res
