class Solution1:
    def numWays(self, n: int, k: int) -> int:
        if n == 1:
            return k
        if n == 2:
            return k * k
        ways_at_index = [0] * (n + 1)
        ways_at_index[1] = k
        ways_at_index[2] = k * k
        for i in range(3, n + 1):
            ways_at_index[i] = (k - 1) * (ways_at_index[i - 1] + ways_at_index[i - 2])
        return ways_at_index[n]

from functools import cache

class Solution2:
    def numWays(self, n: int, k: int) -> int:
        @cache
        def count_ways(i):
            if i == 1:
                return k
            if i == 2:
                return k * k
            return (k - 1) * (count_ways(i - 1) + count_ways(i - 2))
        return count_ways(n)

class Solution3:
    def numWays(self, n: int, k: int) -> int:
        index_to_ways = {}
        def count_ways(i):
            if i == 1:
                return k
            if i == 2:
                return k * k
            if i in index_to_ways:
                return index_to_ways[i]
            index_to_ways[i] = (k - 1) * (count_ways(i - 1) + count_ways(i - 2))
            return index_to_ways[i]
        return count_ways(n)
