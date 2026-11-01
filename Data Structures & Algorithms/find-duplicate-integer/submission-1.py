class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # length = n + 1
        # all values are between [1, len(nums) - 1]

        # i is current node
        # nums[i] is the next node that node i is linked to

        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]

            if slow == slow2:
                return slow
            