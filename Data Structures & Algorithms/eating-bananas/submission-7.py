import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # lowest possible rate = 1
        # highest possible rate = max(piles)

        # hours needed for a pile = math.ceil(pile / rate)

        l = 1
        r = max(piles)
        res = r

        while l <= r:
            rate = int((l + r) / 2)

            hours_needed = 0
            for pile in piles:
                hours_needed += math.ceil(pile / rate)
            
            if hours_needed > h:
                l = rate + 1
            else:
                res = min(res, rate)
                r = rate - 1
        
        return res
