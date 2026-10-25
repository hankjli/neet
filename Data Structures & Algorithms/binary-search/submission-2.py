class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = int((l + r) / 2)
            cur = nums[mid]

            if cur < target:
                l = mid + 1
            elif cur > target:
                r = mid - 1
            else:
                return mid
        
        return -1