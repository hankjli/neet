class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = int((l + r) / 2)
            cur = nums[mid]

            if cur == target:
                return mid

            if cur >= nums[l]:
                # mid is currently in left segment
                if nums[l] <= target <= cur:
                    r = mid
                else:
                    l = mid + 1

            else: # cur < nums[l]
                if target >= nums[l] or target <= cur:
                    r = mid
                else:
                    l = mid + 1

        return -1




