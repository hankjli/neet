class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # have two arrays
        # L, L[i] is product of all elements to left of i in original
        # R, R[i] is prod of all elements to right of i in original

        L = [1] * len(nums)
        R = [1] * len(nums)
        res = [0] * len(nums)

        l_prod = nums[0]
        r_prod = nums[len(nums) - 1]

        for i in range(1, len(nums)):
            r_idx = len(nums) - 1 - i

            L[i] = l_prod
            R[r_idx] = r_prod

            l_prod *= nums[i]
            r_prod *= nums[r_idx]
        
        for i in range(len(nums)):
            res[i] = L[i] * R[i]
        
        return res