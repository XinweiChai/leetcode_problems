from typing import Sequence


class Solution:
    # def fullJustify(self, words: Sequence[str], maxWidth: int) -> Sequence[str]:
    #     text = []
    #     tot = 0
    #     l = 0
    #     r = 0
    #     while r < len(words):
    #         tot += len(words[r])
    #         if tot + r - l > maxWidth:
    #             tot -= len(words[r])
    #             r -= 1
    #             if l == r:
    #                 text.append(words[l] + ' ' * (maxWidth - tot))
    #                 tot = 0
    #                 r += 1
    #                 l = r
    #                 continue
    #             spaces = maxWidth - tot
    #             avg_spaces = spaces // (r - l)
    #             extra_spaces = spaces - (r - l) * avg_spaces
    #             for i in range(extra_spaces):
    #                 words[l + i] += ' '
    #             text.append((' ' * avg_spaces).join(words[l:r + 1]))
    #             tot = 0
    #             l = r + 1
    #         r += 1
    #     text.append(' '.join(words[l:]) + ' ' * (maxWidth - tot - (r - l) + 1))
    #     return text

    # Concise version
    def fullJustify(self, words, maxWidth):
        res, cur, num_of_letters = [], [], 0
        for w in words:
            if num_of_letters + len(w) + len(cur) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    cur[i % (len(cur) - 1 or 1)] += ' '
                res.append(''.join(cur))
                cur, num_of_letters = [], 0
            cur.append(w)
            num_of_letters += len(w)
        return res + [' '.join(cur).ljust(maxWidth)]

# print(Solution().fullJustify(words=["This", "is", "an", "example", "of", "text", "justification."], maxWidth=16))
print(Solution().fullJustify(words=["What", "must", "be", "acknowledgment", "shall", "be"], maxWidth=16))
