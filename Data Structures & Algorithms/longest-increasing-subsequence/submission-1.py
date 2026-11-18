class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # dp[i] = len of longest seq up to element at idx i
        dp = [0] * len(nums)
        dp[0] = 1

        for i in range (1, len(dp)):
            cur = nums[i]

            res = 1
            for j in range(i):
                # for all prev nums
                # if cur > prev, the sequence ending at prev can be
                    # extended by adding on cur
                if cur > nums[j]:
                    res = max(res, dp[j] + 1)
            
            dp[i] = res
        
        return max(dp)