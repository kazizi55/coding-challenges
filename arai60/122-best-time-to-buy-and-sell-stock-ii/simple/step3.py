class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        HAVE_STOCK = 1
        NOT_HAVE_STOCK = 0
        profits = [[0] * 2 for _ in range(len(prices))]
        profits[0][HAVE_STOCK] = -prices[0]
        profits[0][NOT_HAVE_STOCK] = 0
        for i in range(1, len(prices)):
            profits[i][HAVE_STOCK] = max(
                profits[i-1][NOT_HAVE_STOCK] - prices[i],
                profits[i-1][HAVE_STOCK]
            )
            profits[i][NOT_HAVE_STOCK] = max(
                profits[i-1][HAVE_STOCK] + prices[i],
                profits[i-1][NOT_HAVE_STOCK]
            )
        return max(
            profits[-1][HAVE_STOCK],
            profits[-1][NOT_HAVE_STOCK]
        )

class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        yesterday_price = prices[0]
        for i in range(1, len(prices)):
            today_price = prices[i]
            if yesterday_price < today_price:
                max_profit += today_price - yesterday_price
            yesterday_price = today_price
        return max_profit

class Solution3:
    def maxProfit(self, prices: List[int]) -> int:
        def find_next_bottom(from_index):
            index = from_index
            while index < len(prices) - 1 and prices[index] >= prices[index+1]:
                index += 1
            return index
        def find_next_top(from_index):
            index = from_index
            while index < len(prices) - 1 and prices[index] <= prices[index+1]:
                index += 1
            return index
        max_profit = 0
        index = 0
        while index < len(prices) - 1:
            bottom_index = find_next_bottom(index)
            top_index = find_next_top(bottom_index)
            max_profit += prices[top_index] - prices[bottom_index]
            index = top_index + 1
        return max_profit
