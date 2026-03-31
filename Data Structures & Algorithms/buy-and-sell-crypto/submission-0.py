class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = 0
        for L in range(len(prices)):
            for R in range(L + 1, len(prices)):
                if (prices[R] - prices[L]) > diff:
                    diff = prices[R] - prices[L]
        return diff