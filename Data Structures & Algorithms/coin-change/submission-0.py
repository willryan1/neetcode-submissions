class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [10000000000000] * (amount + 1)
        dp[0] = 0
        
        for i in range(len(coins)):
            for j in range(amount + 1):
                if j + coins[i] <= amount:
                    dp[j + coins[i]] = min(dp[j + coins[i]], dp[j] + 1)
        if dp[amount] == 10000000000000:
            return -1
        return dp[amount]