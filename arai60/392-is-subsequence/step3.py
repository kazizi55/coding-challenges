class Solution1:
    def isSubsequence(self, s: str, t: str) -> bool:
        def traverse_s_t(s_index, t_index) -> bool:
            if s_index == len(s):
                return True
            if t_index == len(t):
                return False

            if s[s_index] == t[t_index]:
                return traverse_s_t(s_index + 1, t_index + 1)
            return traverse_s_t(s_index, t_index + 1)
        return traverse_s_t(0, 0)

class Solution2:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_index = 0
        t_index = 0
        while True:
            if len(s) == s_index:
                return True
            if len(t) == t_index:
                return False
            if s[s_index] == t[t_index]:
                s_index += 1
                t_index += 1
                continue
            t_index += 1

class Solution3:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == '':
            return True
        s_index = 0
        for t_char in t:
            if t_char == s[s_index]:
                s_index += 1
                if s_index == len(s):
                    return True
        return False
