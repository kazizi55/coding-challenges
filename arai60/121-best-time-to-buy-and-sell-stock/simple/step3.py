class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        max_profits = [0] * len(prices)
        min_price = prices[0]
        for i in range(1, len(prices)):
            max_profits[i] = max(
                prices[i] - min_price,
                max_profits[i-1]
            )
            min_price = min(
                prices[i],
                min_price
            )
        return max_profits[-1]

class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        min_prices_from_left = [prices[0]] * len(prices)
        for i in range(1, len(prices)):
            if min_prices_from_left[i-1] > prices[i]:
                min_prices_from_left[i] = prices[i]
                continue
            min_prices_from_left[i] = min_prices_from_left[i-1]
        max_prices_from_right = [prices[-1]] * len(prices)
        for i in range(len(prices)-2, -1, -1):
            if max_prices_from_right[i+1] < prices[i]:
                max_prices_from_right[i] = prices[i]
                continue
            max_prices_from_right[i] = max_prices_from_right[i+1]
        max_profit = 0
        for min_price, max_price in zip(min_prices_from_left, max_prices_from_right):
            max_profit = max(
                max_price - min_price,
                max_profit
            )
        return max_profit
    
class Solution3:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            max_profit = max(
                prices[i] - min_price,
                max_profit
            )
            if prices[i] < min_price:
                min_price = prices[i]
        return max_profit
