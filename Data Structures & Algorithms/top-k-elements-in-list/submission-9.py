class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # any num can appear at most len(nums) times

        num_counts = {}
        counts = [[] for i in range(len(nums))]
        res = []

        for num in nums:
            num_counts[num] = num_counts.setdefault(num, 0) + 1
        
        for num, count in num_counts.items():
            counts[count - 1].append(num)
        

        for i in range(len(nums) - 1, -1, -1):
            res.extend(counts[i])

            if len(res) == k:
                break
        
        return res