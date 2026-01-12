class Solution1:
    def firstUniqChar(self, s: str) -> int:
        letter_frequency = defaultdict(int)
        for letter in s:
            letter_frequency[letter] += 1
        for i in range(len(s)):
            if letter_frequency[s[i]] == 1:
                return i
        return -1

class Solution2:
    def firstUniqChar(self, s: str) -> int:
        letter_to_frequency = Counter(s)
        for i, letter in enumerate(s):
            if letter_to_frequency[letter] == 1:
                return i
        return -1
