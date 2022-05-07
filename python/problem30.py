from typing import Sequence


class Solution:
    def findSubstring(self, s: str, words: Sequence[str]) -> Sequence[int]:
        # Iterate over all the substrings
        # length = len(words[0])
        # words_length = length * len(words)
        #
        # def is_valid(pos, words):
        #     while words:
        #         if s[pos:pos + length] in words:
        #             words.remove(s[pos:pos + length])
        #             pos += length
        #         else:
        #             return False
        #     return True
        #
        # index = []
        # cp_words = words
        # for i in range(len(s) - words_length + 1):
        #     words = cp_words.copy()
        #     if is_valid(i, words):
        #         index.append(i)
        # return index

        # if not words or not words[0]:
        #     return []
        # word_frequency = {}
        # result = []
        # for word in words:
        #     if word not in word_frequency:
        #         word_frequency[word] = 0
        #     word_frequency[word] += 1
        #
        # word_count = len(words)
        # word_length = len(words[0])
        # for i in range(len(s) - word_count * word_length + 1):
        #     words_seen = {}
        #     for j in range(word_count):
        #         next_word = i + j * word_length
        #         word = s[next_word: next_word + word_length]
        #         if word not in word_frequency:
        #             break
        #         if word not in words_seen:
        #             words_seen[word] = 0
        #         words_seen[word] += 1
        #         if words_seen[word] > word_frequency.get(word, 0):
        #             break
        #         if j + 1 == word_count:
        #             result.append(i)
        # return result

        # A clever solution using dictionary
        if not s or not words:
            return []
        lenstr = len(s)
        lenword = len(words[0])
        lensubstr = len(words) * lenword
        times = {}
        for word in words:
            if word in times:
                times[word] += 1
            else:
                times[word] = 1
        ans = []

        def findAnswer(strstart, lenstr, lenword, lensubstr):
            wordstart = strstart
            curr = {}
            while strstart + lensubstr <= lenstr:
                word = s[wordstart:wordstart + lenword]
                wordstart += lenword
                if word not in times:
                    strstart = wordstart
                    curr.clear()
                else:
                    if word in curr:
                        curr[word] += 1
                    else:
                        curr[word] = 1
                    while curr[word] > times[word]:
                        curr[s[strstart:strstart + lenword]] -= 1
                        strstart += lenword
                    if wordstart - strstart == lensubstr:
                        ans.append(strstart)

        for i in range(min(lenword, lenstr - lensubstr + 1)):
            findAnswer(i, lenstr, lenword, lensubstr)
        return ans


print(Solution().findSubstring("barfoofoofoobarman", ["foo", "bar"]))
