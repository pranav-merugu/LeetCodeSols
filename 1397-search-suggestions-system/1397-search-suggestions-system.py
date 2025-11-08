from collections import deque

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.words = []
        self.isEndOfWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Method to insert a key into the Trie
    def insert(self, key):
        curr = self.root
        for c in key:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
            curr.words.append(key)
        curr.isEndOfWord = True

    # Method to search a key in the Trie
    def search(self, key):
        curr = self.root
        for c in key:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        return curr.words


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        T = Trie()

        for product in products:
            T.insert(product)
        
        res = []
        cur = ''
        for s in searchWord:
            cur += s
            ans = T.search(cur)
            if ans == False:
                ans = []
            else:
                ans.sort()
            res.append(ans[:3])
        
        return res

