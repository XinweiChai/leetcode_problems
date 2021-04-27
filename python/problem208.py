class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.w_set = set()
        self.w_dict = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype -> None
        """
        self.w_set.add(word)
        cur = self.w_dict
        for i in word:
            if i not in cur:
                cur[i] = {}
            cur = cur[i]

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype -> bool
        """
        return word in self.w_set

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype -> bool
        """
        cur = self.w_dict
        for i in prefix:
            if i in cur:
                cur = cur[i]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)