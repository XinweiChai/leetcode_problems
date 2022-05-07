from typing import Sequence
import collections


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: Sequence[str]) -> Sequence[Sequence[str]]:
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
        if endWord not in wordList:
            return []
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
                            # tree[x].add(y) if rev else tree[y].add(x)
                            # Code using dict
                            if rev:
                                if x in tree:
                                    tree[x].add(y)
                                else:
                                    tree[x] = {y}
                            else:
                                if y in tree:
                                    tree[y].add(x)
                                else:
                                    tree[y] = {x}
            bq, nq = nq, set()
            if len(bq) > len(eq):
                bq, eq, rev = eq, bq, not rev

        def bt(x):
            # For better performance, using dict instead of defaultdict
            if x == beginWord:
                return [[x]]
            else:
                temp = []
                if x in tree:
                    for y in tree[x]:
                        for rest in bt(y):
                            temp.append(rest + [x])
            return temp
            # return [[x]] if x == beginWord else [rest + [x] for y in tree[x] for rest in bt(y)]

        return bt(endWord)


# print(Solution().findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
# print(Solution().findLadders("a", "c", ["a", "b", "c"]))
# print(Solution().findLadders("hot", "dog", ["hot", "dog"]))
print(Solution().findLadders("red", "tax", ["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"]))
