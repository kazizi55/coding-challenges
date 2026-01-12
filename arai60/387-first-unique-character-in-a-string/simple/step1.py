class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_to_index = defaultdict(int)
        duplicated_chars = set()
        for i, char in enumerate(s):
            if char in duplicated_chars:
                continue
            if char in char_to_index:
                char_to_index.pop(char)
                duplicated_chars.add(char)
                continue
            char_to_index[char] = i
        values = list(char_to_index.values())
        if len(values) == 0:
            return -1
        return sorted(values)[0]
