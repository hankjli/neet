class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # nums[i] + nums[j] == target
        # nums[i] == target - nums[j]

        seen = {}

        for i in range(len(nums)):
            comp = target - nums[i]

            if comp in seen:
                return [seen[comp], i]
            
            seen[nums[i]] = i