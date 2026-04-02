class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen_char = set()
        max_length = 0
        for right in range(len(s)):
            while s[right] in seen_char:
                seen_char.remove(s[left])
                left += 1
            seen_char.add(s[right])
            max_length = max(max_length, right - left + 1)
        return max_length

class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        last_char_to_index = {}
        max_length = 0
        for right in range(len(s)):
            left = max(left, last_char_to_index.get(s[right], -1) + 1)
            last_char_to_index[s[right]] = right
            max_length = max(max_length, right - left + 1)
        return max_length
