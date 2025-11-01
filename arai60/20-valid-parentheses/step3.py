class Solution:
    def isValid(self, s: str) -> bool:
        stack = ["*"]
        bracket_pairs = {"(": ")", "{": "}", "[": "]", "*": ""}

        for char in s:
            if char in bracket_pairs:
                stack.append(char)
                continue
            if char != bracket_pairs[stack[-1]]:
                return False
            stack.pop()
        return len(stack) == 1
