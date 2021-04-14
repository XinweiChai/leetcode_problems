from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_dict = {beginWord: [0, [[beginWord]]]}
        for i in wordList:
            word_dict[i] = [float('inf'), [[]]]
        wordList = set(wordList)
        cur = [beginWord]
        length = 1
        while cur:
            temp = []
            for i in cur:
                for j in range(len(i)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        next_word = i[:j] + c + i[j + 1:]
                        if next_word in wordList:
                            new_path = [k + [next_word] for k in word_dict[i][1]]
                            if length < word_dict[next_word][0]:
                                word_dict[next_word] = [length, [new_path]]
                            elif length == word_dict[next_word][0]:
                                word_dict[next_word][1].append(new_path)
                            temp.append(next_word)
            cur = temp
            length += 1
        return word_dict[endWord][1]


print(Solution().findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
