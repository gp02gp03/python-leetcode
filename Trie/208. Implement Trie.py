'''
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tree = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        ite = self.tree
        for c in word:
            if c not in ite:
                ite[c] = {}
            ite = ite[c]
        ite['#'] =  '#'
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        ite = self.tree
        for c in word:
            if c not in ite:
                return False
            ite = ite[c]
        return True if '#' in ite else False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        ite = self.tree
        for c in prefix:
            if c not in ite:
                return False
            ite = ite[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
'''
