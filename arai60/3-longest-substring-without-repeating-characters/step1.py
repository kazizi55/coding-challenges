# Wrong Answer　395 / 988 testcases passed
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        current_len = 0
        char_set = set()
        for char in s:
            if char in char_set:
                char_set = set()
                current_len = 1
                max_len = max(max_len, current_len)
                continue
            current_len += 1
            max_len = max(max_len, current_len)
            char_set.add(char)
        return max_len
