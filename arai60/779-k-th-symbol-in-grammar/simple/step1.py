# Time Limit Exceeded 15 / 55 testcases passed
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        row = "0"
        for _ in range(1, n):
            next_row = ""
            for r in row:
                if r == "0":
                    next_row += "01"
                    continue
                next_row += "10"
            row = next_row
        return int(row[k-1])

