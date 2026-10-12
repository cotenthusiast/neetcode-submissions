class PrefixTree:

    def __init__(self):
        self.root = Node(None)
        

    def insert(self, word: str) -> None:
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
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                return False
        return node.is_end
    

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c in node.children:
                node = node.children[c]
            else:
                return False
        return True



class Node:

    def __init__(self, character, is_end = False):
        self.val = character
        self.children = {}
        self.is_end = is_end # defaults to False unless overriden