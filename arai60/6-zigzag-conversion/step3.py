class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= numRows or numRows == 1:
            return s
        rows = [[] for _ in range(numRows)]
        row = 0
        is_going_down = True
        for ch in s:
            rows[row].append(ch)
            if row == 0:
                is_going_down = True
            if row == numRows - 1:
                is_going_down = False
            if is_going_down == True:
                row += 1
                continue
            row -= 1
        return "".join(["".join(row) for row in rows])