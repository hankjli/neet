class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []

        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            base = nums[i]
            
            # target = -base
            # sorting allows use of two pointer approach for 2 sum

            l = i + 1
            r = len(nums) - 1

            while l < r:
                cur = nums[l] + nums[r]

                if cur > -base:
                    r -= 1
                elif cur < -base:
                    l += 1
                else:
                    res.append([base, nums[l], nums[r]])

                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
            
        return res