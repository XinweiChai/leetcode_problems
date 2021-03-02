class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        length = len(words[0])
        words_length = sum([len(i) for i in words])
        def is_valid(pos, words):
            # if not words:
            #     return True
            # if s[pos:pos + length] in words:
            #     words.remove(s[pos:pos + length])
            #     pos += length
            #     return is_valid(pos, words)
            # else:
            #     return False
            while words:
                if s[pos:pos + length] in words:
                    words.remove(s[pos:pos + length])
                    pos += length
                else:
                    return False
            return True

        index = []
        cp_words = words
        for i in range(len(s)):
            if len(s) - words_length < i:
                break
            words = cp_words.copy()
            if is_valid(i, words):
                index.append(i)
        return index


print(Solution().findSubstring("barfoothefoobarman", ["foo","bar"]))