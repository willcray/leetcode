"""
https://leetcode.com/problems/implement-trie-prefix-tree/
time: see functions
space: see functions
Author: Will Cray
Date: 3/14/2022
"""

class TrieNode:
    def __init__(self):
        self.is_end_of_word = False
        self.children = {}

        
class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        
        # time: O(M), where M is len(word)
        # space: O(M)
        
        node = self.root
        
        # iterate each char in word
        for char in word:
            
            # if current char is None in children, construct new TrieNode for the character
            if char not in node.children:
                node.children[char] = TrieNode()
            
            # iterate to next level
            node = node.children[char]
        
        # mark final character as end of word
        node.is_end_of_word = True
            

    def search(self, word: str) -> bool:
        
        # time: O(M), where M is len(word)
        # space: O(1)
        
        node = self.root
        
        # iterate through trie, checking each character
        for char in word:
            
            # if character doesn't exist, return false
            if char not in node.children:
                return False
                
            node = node.children[char]
            
        # only return True if every character is in trie and the end of the word is marked
        return node.is_end_of_word
        
        
    def startsWith(self, prefix: str) -> bool:
        
        node = self.root
        
        # iterate string
        for char in prefix:
            
            # return False if char doesn't exist in Trie
            if char not in node.children:
                return False
            
            node = node.children[char]
            
        return True
        
        
        
        
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)