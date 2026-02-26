class Solution1:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def is_breakable(from_index):
            if from_index == len(s):
                return True
            for word in wordDict:
                if not s.startswith(word, from_index):
                    continue
                if is_breakable(from_index + len(word)):
                    return True
            return False
        return is_breakable(0)

class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        is_breakable_at_length = [False] * (len(s)+1)
        is_breakable_at_length[0] = True
        for i in range(len(s)):
            if not is_breakable_at_length[i]:
                continue
            for word in wordDict:
                if not s.startswith(word, i):
                    continue
                is_breakable_at_length[i+len(word)] = True
        return is_breakable_at_length[-1]
