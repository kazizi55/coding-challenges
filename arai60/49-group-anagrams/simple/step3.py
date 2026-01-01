class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        common_key_to_words = defaultdict(list)
        for s in strs:
            common_key = tuple(sorted(s))
            common_key_to_words[common_key].append(s)
        return list(common_key_to_words.values())

class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        common_key_to_words = defaultdict(list)
        for s in strs:
            common_key = "".join(sorted(s))
            common_key_to_words[common_key].append(s)
        return list(common_key_to_words.values())
