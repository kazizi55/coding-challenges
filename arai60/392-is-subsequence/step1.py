class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == t:
            return True
        s_index = 0
        for t_char in t:
            if s_index == len(s):
                return True
            if t_char == s[s_index]:
                s_index += 1
                if s_index == len(s):
                    return True                
        return False

class RevisedSolution:
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
