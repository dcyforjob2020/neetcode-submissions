class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()

            cur = cur.children[c]

        cur.end = True

    def search(self, word: str) -> bool:
        res = False

        cur = self.root

        n = len(word)

        def dfs(i, node):
            nonlocal res
            
            if i >= n:
                return

            c = word[i]

            if not node:
                return

            if i == n - 1:
                if c == ".":
                    for e in node.children:
                        if node.children[e].end:
                            res = True

                            return

                if c in node.children and node.children[c].end:
                    res = True

                    return

            if c == ".":
                for e in node.children:
                    dfs(i + 1, node.children[e])

                    if res:
                        return

            if c in node.children:
                dfs(i + 1, node.children[word[i]])

        dfs(0, cur)

        return res
