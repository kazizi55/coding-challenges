class Solution1:
    def uniquePaths(self, m: int, n: int) -> int:
        nums_of_paths = [[0] * n for _ in range(m)]
        for c in range(n):
            nums_of_paths[0][c] = 1
        for r in range(1, m):
            for c in range(n):
                if c == 0:
                    nums_of_paths[r][c] = 1
                    continue
                nums_of_paths[r][c] = nums_of_paths[r - 1][c] + nums_of_paths[r][c - 1]
        return nums_of_paths[-1][-1]

class Solution1Prime:
    def uniquePaths(self, m: int, n: int) -> int:
        nums_of_paths = [[0] * n for _ in range(m)]
        for r in range(m):
            nums_of_paths[r][0] = 1
        for c in range(n):
            nums_of_paths[0][c] = 1
        for r in range(1, m):
            for c in range(1, n):
                nums_of_paths[r][c] = nums_of_paths[r - 1][c] + nums_of_paths[r][c - 1]
        return nums_of_paths[-1][-1]

class Solution1Prime2:
    def uniquePaths(self, m: int, n: int) -> int:
        nums_of_paths = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                if r == 0 or c == 0:
                    nums_of_paths[r][c] = 1
                    continue
                nums_of_paths[r][c] = nums_of_paths[r - 1][c] + nums_of_paths[r][c - 1]
        return nums_of_paths[-1][-1]

class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        nums_of_paths = [0] * n
        nums_of_paths[0] = 1
        for _ in range(m):
            for c in range(n):
                if c == 0:
                    continue
                nums_of_paths[c] += nums_of_paths[c - 1]
        return nums_of_paths[-1]

class Solution2Prime:
    def uniquePaths(self, m: int, n: int) -> int:
        nums_of_paths = [1] * n
        for _ in range(1, m):
            for c in range(1, n):
                nums_of_paths[c] += nums_of_paths[c - 1]
        return nums_of_paths[-1]

class Solution3:
    def uniquePaths(self, m: int, n: int) -> int:
        def factorial(k: int):
            if k == 0:
                return 1
            return k * factorial(k - 1)
        combination = factorial(m + n - 2) // (factorial(m - 1) * factorial(n - 1))
        return combination

class Solution4:
    def uniquePaths(self, m: int, n: int) -> int:
        return comb(m + n - 2, m - 1)

class Solution5:
    @cache
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
