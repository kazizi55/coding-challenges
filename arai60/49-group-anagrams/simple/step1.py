class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def toSortedStr(val):
            return "".join(sorted(val))

        chars_to_anagrams = defaultdict(list)
        for string in strs:
            anagram_keys = chars_to_anagrams.keys()
            sortedStr = toSortedStr(string)
            if len(anagram_keys) == 0 or not(sortedStr in anagram_keys):
                chars_to_anagrams[sortedStr] = []
            
            chars_to_anagrams[sortedStr].append(string)
        return list(chars_to_anagrams.values())

class ImprovedSolution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        chars_to_anagrams = defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s))
            chars_to_anagrams[sorted_s].append(s)
        return list(chars_to_anagrams.values())
