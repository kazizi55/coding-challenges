class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def get_keys_from_word(word) -> List[str]:
            keys = []
            for index in range(len(word)):
                key = (word[:index], word[index + 1:])
                keys.append(key)
            return keys
        
        key_to_words = defaultdict(list)
        for word in wordList:
            for key in get_keys_from_word(word):
                key_to_words[key].append(word)
        depth = 0
        traversed_words = set()
        words_in_depth = [beginWord]
        while words_in_depth:
            depth += 1
            words_in_next_depth = []
            for word in words_in_depth:
                if word == endWord:
                    return depth
                if word in traversed_words:
                    continue
                traversed_words.add(word)
                for key in get_keys_from_word(word):
                    next_words = key_to_words[key]
                    words_in_next_depth.extend(next_words)
            words_in_depth = words_in_next_depth
        return 0
