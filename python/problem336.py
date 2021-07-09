from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        # False means the word is not reversed, True means the word is reversed
        buckets = sorted([(w, False, i) for i, w in enumerate(words)] +
                         [(w[::-1], True, i) for i, w in enumerate(words)])
        length, result = len(buckets), []
        for i, (word, rev, idx) in enumerate(buckets):
            for j in range(i + 1, length):
                next_word, next_rev, next_idx = buckets[j]
                if next_word.startswith(word):
                    if idx != next_idx and rev != next_rev:
                        rest = next_word[len(word):]
                        if rest == rest[::-1]:
                            if next_rev:
                                result.append([idx, next_idx])
                            else:
                                result.append([next_idx, idx])
                else:
                    break
        return result


if __name__ == '__main__':
    print(Solution().palindromePairs(words=["a", "aa"]))
