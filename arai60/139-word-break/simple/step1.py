# 18 / 48 testcases passed
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        for i in range(len(s)):
            if not s[:i] in wordDict:
                continue
            if len(s[i:]) == 0:
                return True
            return self.wordBreak(s[i:], wordDict)
        return False

class RevisedSolution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def word_break(sub_s: str):
            if len(sub_s) == 0:
                return True
            for i in range(1, len(sub_s)+1):
                if not sub_s[:i] in wordDict:
                    continue
                if word_break(sub_s[i:]):
                    return True
            return False
        return word_break(s)
