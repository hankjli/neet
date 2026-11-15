class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # dp[i] = max money possible up to and including ith house
        dp = [0] * (len(nums) + 1)
        dp[0] = 0
        dp[1] = nums[0]

        for i in range(2, len(dp)):
            cur = nums[i - 1]

            dp[i] = max(dp[i - 2] + cur, dp[i - 1])
        
        return dp[-1]