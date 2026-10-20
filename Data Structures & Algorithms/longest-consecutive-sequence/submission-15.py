class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0

        nums_set = set(nums)
        possible_starts = set()

        for num in nums:
            if num - 1 not in nums_set:
                possible_starts.add(num)
        
        for num in possible_starts:
            cur = 1

            while num + 1 in nums_set:
                cur += 1
                num += 1
            
            res = max(res, cur)

        return res