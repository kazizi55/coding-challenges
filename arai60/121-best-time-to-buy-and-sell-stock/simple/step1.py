class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        max_profits = [0] * len(prices)
        max_profits[0] = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            max_profits[i] = max(
                max_profits[i-1],
                prices[i] - min_price
            )
        return max_profits[-1]
