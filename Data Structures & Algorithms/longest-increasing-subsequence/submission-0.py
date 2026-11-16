class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = [0] * len(nums)
        dp[0] = 1

        # dp[i] = length of longest inc subsequence ending at idx i

        for i in range(1, len(dp)):
            res = 1
            for j in range(i):
                # for every previous element
                # if nums[i] > nums[j]
                # then a sequence ending at idx j can be extended by
                    # the num at idx i 
                prev_end = nums[j]
                if nums[i] > nums[j]:
                    res = max(res, dp[j] + 1)
            
            dp[i] = res
        
        return max(dp)