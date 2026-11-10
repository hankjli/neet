class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        
        dp1 = [0] * (len(nums) + 1)
        dp1[1] = nums[0]

        # firt find max amount when considering first and not last
        for i in range(2, len(dp1) - 1):
            skip_cur = dp1[i - 1]
            rob_cur = dp1[i - 2] + nums[i - 1]

            dp1[i] = max(skip_cur, rob_cur)


        # then find max when considering last and not first
        dp2 = [0] * (len(nums) + 1)
        for i in range(2, len(dp2)):
            skip_cur = dp2[i - 1]
            rob_cur = dp2[i - 2] + nums[i - 1]

            dp2[i] = max(skip_cur, rob_cur)

        print(dp1)
        print(dp2)
        return max(dp1[-2], dp2[-1])