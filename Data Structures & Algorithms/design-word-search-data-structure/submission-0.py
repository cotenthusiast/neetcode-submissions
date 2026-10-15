class WordDictionary:

    def __init__(self):
        self.root = Node(None)

    def addWord(self, word: str) -> None:
        if word is None:
            return 
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                node.children[c] = Node(c)
                node = node.children[c]
        node.is_end = True

    def search(self, word: str) -> bool:

        def dfs(i, node):
            if len(word) == i:
                return node.is_end

            if word[i] != ".":
                if word[i] in node.children:
                    node = node.children[word[i]]
                    return dfs(i + 1, node)
                else:
                    return False

            for child in node.children.values():
                if dfs(i + 1, child):
                    return True

            return False

        node = self.root

        for i, c in enumerate(word):
            if c == ".":
                return dfs(i, node)

            if c in node.children:
                node = node.children[c]
            else:
                return False

        return node.is_end

class Node:

    def __init__(self, character, is_end = False):
        self.val = character
        self.children = {}
        self.is_end = is_end # defaults to False unless overriden