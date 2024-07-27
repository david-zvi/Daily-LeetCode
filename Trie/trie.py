# Solved on 27/07/2024
# https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode:
    def __init__(self):
        self.next = dict()
        self.word_end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        temp = self.root
        for letter in word:
            if letter not in temp.next: temp.next[letter] = TrieNode()
            temp = temp.next[letter]
        temp.word_end = True

    def search(self, word: str) -> bool:
        temp = self.root
        for letter in word:
            if letter not in temp.next: return False
            temp = temp.next[letter]
        return temp.word_end

    def startsWith(self, prefix: str) -> bool:
        temp = self.root
        for letter in prefix:
            if letter not in temp.next: return False
            temp = temp.next[letter]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
