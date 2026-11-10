class Solution:
    def rob(self, nums: List[int]) -> int:

        dp = [0] * (len(nums) + 1)
        dp[0] = 0
        dp[1] = nums[0]

        # [1, 5, 2, 3, 150]
        # [0, 1, 0, 0, 0, 0]

        for i in range(2, len(dp)):
            skip_cur = dp[i - 1]
            rob_cur = dp[i - 2] + nums[i - 1]

            dp[i] = max(skip_cur, rob_cur)

        return dp[-1]