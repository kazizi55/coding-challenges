class Solution:
    def myAtoi(self, s: str) -> int:
        index = 0
        while index < len(s) and s[index] == " ":
            index += 1
        if index == len(s):
            return 0
        
        sign = 1
        if s[index] == "+":
            index += 1
        elif s[index] == "-":
            sign *= -1
            index += 1
        
        num = 0
        MIN_INT = -2 ** 31
        MAX_INT = 2 ** 31 - 1
        while index < len(s) and ord("0") <= ord(s[index]) <= ord("9"):
            digit = ord(s[index]) - ord("0")
            num = num * 10 + sign * digit
            if num > MAX_INT:
                return MAX_INT
            if num < MIN_INT:
                return MIN_INT
            index += 1
        return num