from typing import List
import collections


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # One-way BFS
        # wordList = set(wordList)
        # wordList.discard(beginWord)
        # len_word = len(beginWord)
        # if endWord not in wordList:
        #     return []
        # word_dict = {beginWord: [[beginWord]]}
        # cur = {beginWord}
        # found = False
        # while cur and not found:
        #     temp = set()
        #     cur_words = set()
        #     for i in cur:
        #         for j in range(len_word):
        #             for c in 'abcdefghijklmnopqrstuvwxyz':
        #                 next_word = i[:j] + c + i[j + 1:]
        #                 if next_word == endWord:
        #                     found = True
        #                 if next_word in wordList:
        #                     cur_words.add(next_word)
        #                     new_path = [k + [next_word] for k in word_dict[i]]
        #                     if next_word not in word_dict:
        #                         word_dict[next_word] = new_path
        #                     else:
        #                         word_dict[next_word] += new_path
        #                     temp.add(next_word)
        #     wordList -= cur_words
        #     cur = temp
        # return word_dict[endWord] if found else []

        # Two-way BFS
        tree, wordList, n = collections.defaultdict(set), set(wordList), len(beginWord)
        if endWord not in wordList: return []
        found, bq, eq, nq, rev = False, {beginWord}, {endWord}, set(), False
        while bq and not found:
            wordList -= set(bq)
            for x in bq:
                for i in range(n):
                    first, second = x[:i], x[i + 1:]
                    for c in 'qwertyuiopasdfghjklzxcvbnm':
                        y = first + c + second
                        if y in wordList:
                            if y in eq:
                                found = True
                            else:
                                nq.add(y)
                            tree[y].add(x) if rev else tree[x].add(y)
            bq, nq = nq, set()
            if len(bq) > len(eq):
                bq, eq, rev = eq, bq, not rev

        def bt(x):
            return [[x]] if x == endWord else [[x] + rest for y in tree[x] for rest in bt(y)]

        return bt(beginWord)


# print(Solution().findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
# print(Solution().findLadders("a", "c", ["a", "b", "c"]))
# print(Solution().findLadders("hot", "dog", ["hot", "dog"]))
print(Solution().findLadders("red", "tax", ["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"]))
