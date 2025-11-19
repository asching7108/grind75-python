# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

class Node:
    def __init__(self, char="", children=None, isLeaf=False):
        self.char = char
        self.isLeaf = isLeaf
        self.children = children if children else {}

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        ptr = self.root
        for char in word:
            if char not in ptr.children:
                ptr.children[char] = Node(char)
            ptr = ptr.children[char]
        ptr.isLeaf = True

    # Time complexity: O(n) where n is the length of word
    # Space complexity: O(n)

    def search(self, word: str) -> bool:
        ptr = self.root
        for char in word:
            if char not in ptr.children:
                return False
            ptr = ptr.children[char]
        return ptr.isLeaf

    # Time complexity: O(n) where n is the length of word
    # Space complexity: O(1)

    def startsWith(self, prefix: str) -> bool:
        ptr = self.root
        for char in prefix:
            if char not in ptr.children:
                return False
            ptr = ptr.children[char]
        return True

    # Time complexity: O(n) where n is the length of prefix
    # Space complexity: O(1)