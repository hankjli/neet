class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = prices[0]

        res = 0

        for r in range(1, len(prices)):

            profit = prices[r] - buy
            res = max(res, profit)

            buy = min(prices[r], buy)
        
        return res

