# TLE
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        if n < 0:
            return 1 / (self.myPow(x, -n - 1) * self.myPow(x, -n - 2))
        return self.myPow(x, n - 1) * self.myPow(x, n - 2)

class RevisedSolution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n < 0:
            return 1 / self.myPow(1/x, -n)
        if n % 2 == 1:
            return x * self.myPow(x, n - 1)
        return self.myPow(x ** 2, n // 2)
