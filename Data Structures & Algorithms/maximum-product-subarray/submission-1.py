class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        prev_max = 1
        prev_min = 1
        res = nums[0]

        for num in nums:
            if num == 0:
                prev_max = 1
                prev_min = 1

            tmp = prev_max
            prev_max = max(num, prev_max * num, prev_min * num)
            prev_min = min(num, tmp * num, prev_min * num)

            res = max(res, prev_max)


        return res