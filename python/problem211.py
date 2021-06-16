class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}

    def addWord(self, word: str) -> None:
        cur = self.d
        for i in word:
            if i not in cur:
                cur[i] = {}
            cur = cur[i]
        cur['#'] = None

    def search(self, word: str) -> bool:
        def rec(pos, cur):
            if pos == len(word):
                return '#' in cur
            if word[pos] == '.':
                return any([rec(pos + 1, cur[i]) for i in cur.keys()])
            else:
                return word[pos] in cur and rec(pos + 1, cur[word[pos]])

        return rec(0, self.d)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

if __name__ == '__main__':
    obj = WordDictionary()
    obj.addWord('abc')
    param_2 = obj.search('ab')
    print(param_2)
