class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, len(dp)):
            min_needed = None
            for coin in coins:
                if (i - coin) >= 0:
                    if min_needed is None and dp[i - coin] != amount + 1:
                        min_needed = dp[i - coin] + 1
                    elif min_needed is not None:
                        min_needed = min(min_needed, dp[i - coin] + 1)
            
            dp[i] = min_needed if min_needed is not None else amount + 1


        print(dp)
        return dp[-1] if dp[-1] != amount + 1 else -1