class Solution1:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        if k % 2 == 1:
            return self.kthGrammar(n - 1, (k+1) // 2)
        return 1 - self.kthGrammar(n - 1, (k+1) // 2)

class Solution2:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        half_length = 2 ** (n-2)
        if k > half_length:
            return 1 - self.kthGrammar(n-1, k - half_length)
        return self.kthGrammar(n-1, k)
