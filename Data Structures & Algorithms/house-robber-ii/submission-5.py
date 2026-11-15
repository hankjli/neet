class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # first consider/disregard first/last house
        # dp1[i] = max money possible at (i-1th) house
        dp1 = [0] * len(nums)
        dp1[0] = 0
        dp1[1] = nums[0]
        for i in range(2, len(dp1)):
            dp1[i] = max(dp1[i - 2] + nums[i - 1], dp1[i - 1])
        
        # then disregard/consider first/last house
        # dp2[i] = max money possible at ith house
        dp2 = [0] * len(nums)
        dp2[0] = 0
        dp2[1] = nums[1]
        for i in range(2, len(dp2)):
            dp2[i] = max(dp2[i - 2] + nums[i], dp2[i - 1])
        
        print(dp1)
        print(dp2)
        return max(dp1[-1], dp2[-1])