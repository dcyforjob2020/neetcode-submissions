class TrieNode:
    def __init__(self):
        self.children = {}

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        self.hashset = set()
        

    def insert(self, word: str) -> None:
        self.hashset.add(word)

        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()

            cur = cur.children[c]

    def search(self, word: str) -> bool:
        return word in self.hashset
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False

            cur = cur.children[c]

        return True

                
        