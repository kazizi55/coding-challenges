# 途中までしか解けず。
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        num_of_words_in_shortest_transformation_seq = 0
        if not(endWord in wordList):
            return num_of_words_in_shortest_transformation_seq
        