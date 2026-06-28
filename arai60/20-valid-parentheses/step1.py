# Wrong Answer 76 / 103 testcases passed
class Solution:
    def isValid(self, s: str) -> bool:
        BRACKET_PAIRS = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        last_index = -1
        for c, index in enumerate(s):
            if index == len(s) // 2 + 1:
                break
            if not c in list(BRACKET_PAIRS):
                return False
            if not s[last_index] == BRACKET_PAIRS[c]:
                return False
            last_index -= 1
        return True
            
class SolutionWithStack:
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

class SolutionWithStackAndSentinel:
    def isValid(self, s: str) -> bool:
        open_to_close = { "(": ")", "{": "}", "[": "]", "": "" }
        open_brackets = [""]
        for ch in s:
            if ch in open_to_close:
                open_brackets.append(ch)
                continue
            expected_close_bracket = open_to_close[open_brackets[-1]]
            if ch == expected_close_bracket:
                open_brackets.pop()
                continue
            return False
        return len(open_brackets) == 1