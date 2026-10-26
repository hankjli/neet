class Solution:
    def findMin(self, nums: List[int]) -> int:
        # want to find the right segment
        # [3, 4, 5, 1, 2]

        l = 0
        r = len(nums) - 1

        while l < r:
            mid = int((l + r) / 2)
            cur = nums[mid]

            if cur < nums[l]:
                # the num on the left is > num to the right
                # the split must be between l and mid
                r = mid
            elif cur > nums[l]:
                # num on the right is > num on the left
                # normal, could potentially be in upper/lower segment
                if cur < nums[r]:
                    # currently in the lower segment
                    # regular bsearch basically
                    r = mid - 1
                else: # cur >= r
                    # currently in the upper segment
                    # split must be between mid and return
                    l = mid + 1

            else:
                return min(nums[l], nums[r])
        
        return nums[l]
