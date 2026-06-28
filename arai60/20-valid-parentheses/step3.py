class Solution:
    def isValid(self, s: str) -> bool:
        open_to_close = { "(": ")", "{": "}", "[": "]" }
        open_brackets = []
        for ch in s:
            if ch in open_to_close:
                open_brackets.append(ch)
                continue
            if len(open_brackets) == 0:
                return False
            expected_close_bracket = open_to_close[open_brackets[-1]]
            if ch == expected_close_bracket:
                open_brackets.pop()
                continue
            return False
        return len(open_brackets) == 0