class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums) - 1

        while l <= r:

            if nums[l] <= nums[r]:
                return nums[l]


            mid = int((l + r) / 2)
            cur = nums[mid]

            if cur >= nums[l]:
                # m is in the left segment, min must be [m + 1, r]
                l = mid + 1
            else: # cur < nums[l]
                # min must be between (l, m]
                r = mid