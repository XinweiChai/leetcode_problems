import collections


class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        q = collections.deque([[beginWord, 1]])
        while q:
            word, length = q.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i + 1:]
                    if next_word in wordList:
                        wordList.remove(next_word)
                        q.append([next_word, length + 1])
        return 0


print(Solution().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
# print(Solution().ladderLength("hot", "dog", ["hot", "dog"]))
