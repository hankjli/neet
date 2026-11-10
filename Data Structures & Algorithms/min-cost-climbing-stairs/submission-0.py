class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        dp = [0] * (len(cost) + 1)

        for i in range(2, len(dp)):

            jump2 = dp[i - 2] + cost[i - 2]
            jump1 = dp[i - 1] + cost[i - 1]

            dp[i] = min(jump2, jump1)
        

        return dp[-1]
