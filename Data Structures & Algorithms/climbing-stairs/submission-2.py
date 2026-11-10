class Solution:
    def climbStairs(self, n: int) -> int:

        # for step i, the total ways to get to step i =
        # total ways to get to step i - 1 + ways to get to step i - 2

        # since to get to step i you can either jump 1 step from
        # step i - 1 or jump 2 steps from tep i - 2


        dp = [0] * (n + 1)

        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]
        
        return dp[-1]