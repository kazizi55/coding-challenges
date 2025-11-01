class SolutionWithBracketPairsAndSentinel:
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

class SolutionWithReversedBracketPairs:
    def isValid(self, s: str) -> bool:
        stack = ["*"]
        bracket_pairs = {")": "(", "}": "{", "]": "[", "": "*"}

        for char in s:
            if char in bracket_pairs and stack:
                last_stack = stack.pop()
                if last_stack != bracket_pairs[char]:
                    return False
            else:
                stack.append(char)
        return len(stack) == 1

class SolutionWithBracketWithoutSentinel:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_pairs = {"(": ")", "{": "}", "[": "]"}

        for char in s:
            if char in bracket_pairs:
                stack.append(char)
                continue
            if stack:
                if char != bracket_pairs[stack[-1]]:
                    return False
                else:
                    stack.pop()
            else:
                return False
        return not stack
