# bracket pairs と sentinel を使って実装する version (expected_closing_bracket の命名を追加)
class Solution1:
    def isValid(self, s: str) -> bool:
        bracket_pairs = {"(": ")", "{": "}", "[": "]", "*": ""}
        stack = ["*"]

        for char in s:
            if char in bracket_pairs:
                stack.append(char)
                continue
            expected_closing_bracket = bracket_pairs[stack[-1]]
            if char == expected_closing_bracket:
                stack.pop()
                continue
            return False
        return len(stack) == 1

# bracket pairs を使って実装する version (expected_closing_bracket の命名を追加し、else を使わない)
class Solution2:
    def isValid(self, s: str) -> bool:
        bracket_pairs = {"(": ")", "{": "}", "[": "]"}
        stack = []

        for char in s:
            if char in bracket_pairs:
                stack.append(char)
                continue
            if not stack:
                return False
            expected_closing_bracket = bracket_pairs[stack[-1]]
            if char == expected_closing_bracket:
                stack.pop()
                continue
            return False
        return not stack
