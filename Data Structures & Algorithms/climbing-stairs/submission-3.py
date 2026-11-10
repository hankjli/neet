class Solution:
    def climbStairs(self, n: int) -> int:

        # for step i, the total ways to get to step i =
        # total ways to get to step i - 1 + ways to get to step i - 2

        # since to get to step i you can either jump 1 step from
        # step i - 1 or jump 2 steps from tep i - 2

        two_prev = 1
        one_prev = 1

        for i in range(n - 1):
            temp = two_prev

            two_prev += one_prev
            one_prev = temp

        return two_prev