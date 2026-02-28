# TLE
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def get_necessary_coin_num(coin, amount_) -> int:
            total = amount_
            diff = total - coin
            if diff == 0:
                return 1
            coin_num = 0
            for c in coins:
                coin_num += get_necessary_coin_num(c, diff)
        for c in coins:
            total_coin_num = get_necessary_coin_num(c, amount)
            if total_coin_num > 0:
                return total_coin_num
        return -1

class RevisedSolution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        @cache
        def get_necessary_coin_num(coin, amount_) -> int:
            if amount_ < coin:
                return math.inf
            diff = amount_ - coin
            if diff == 0:
                return 1
            min_coin_num = math.inf
            for c in coins:
                coin_num = get_necessary_coin_num(c, diff)
                if coin_num != math.inf:
                    min_coin_num = min(min_coin_num, coin_num + 1)
            return min_coin_num
        
        ans = math.inf
        for c in coins:
            ans = min(ans, get_necessary_coin_num(c, amount))
        if ans == math.inf:
            return -1
        return int(ans)
