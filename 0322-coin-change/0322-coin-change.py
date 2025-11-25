class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Bottom-up dynamic programming
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[amount] if dp[amount]  != float('inf') else -1

        # Time complexity: O(S * n) where S is the amount, n is the number of coins
        # Space complexity: O(S)