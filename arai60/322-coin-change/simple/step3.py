class Solution1:
    def coinChange(self, coins: List[int], amount: int) -> int:
        num_rows = len(coins) + 1
        num_cols = amount + 1
        min_num_coins = [[math.inf] * num_cols for _ in range(num_rows)]
        min_num_coins[0][0] = 0
        for r in range(1, num_rows):
            for c in range(num_cols):
                if c < coins[r-1]:
                    min_num_coins[r][c] = min_num_coins[r-1][c]
                    continue
                min_num_coins[r][c] = min(
                    min_num_coins[r-1][c],
                    min_num_coins[r][c-coins[r-1]] + 1
                )
        if min_num_coins[-1][-1] == math.inf:
            return -1
        return min_num_coins[-1][-1]

class Solution2:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_num_coin = [math.inf] * (amount + 1)
        min_num_coin[0] = 0
        for coin in coins:
            for amount_ in range(1, amount + 1):
                if amount_ < coin:
                    continue
                min_num_coin[amount_] = min(
                    min_num_coin[amount_],
                    min_num_coin[amount_ - coin] + 1
                )
        if min_num_coin[-1] == math.inf:
            return -1
        return min_num_coin[-1]
