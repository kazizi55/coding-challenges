class Solution1:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n < 0:
            x = 1.0 / x
            n = -n
        if n % 2 == 1:
            return x * self.myPow(x, (n-1) // 2) ** 2
        return self.myPow(x, n // 2) ** 2

class Solution2:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n < 0:
            x = 1/x
            n = -n
        result = 1
        bi = 1
        while bi <= n:
            result *= (x ** bi)
            n -= bi
            bi *= 2
        if n > 0:
            result *= (x ** n)
        return result
