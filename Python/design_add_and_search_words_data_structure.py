"""
https://leetcode.com/problems/design-add-and-search-words-data-structure/
Author: Will Cray
Date: 3/18/2022
Time: see functions
Space: see functions
"""

# trie implementation

class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        # time: O(N), where N is len(word)
        # space: O(N)
        
        node = self.trie
        
        for char in word:
            if char not in node:
                node[char] = {}
                
            node = node[char]
                
        # marks end of word
        node['$'] = True

        
    def search(self, word: str) -> bool:
        # time: O(N), where N is len(word) for words with no dots
        # time: O(26^N) for worst case
        # space: O(M) for worst case due to recursion stack
        
        def search_from_node(word, node) -> bool:
            for i, char in enumerate(word):
                
                if char not in node:
                    if char == '.':
                        # if node is '.', check all possible child routes
                        for child in node:
                            if child != '$' and search_from_node(word[i+1:], node[child]):
                                return True
                    
                    # no nodes produced answer
                    return False
                
                # character found, continue to next
                else:
                    node = node[char]

            return '$' in node

        return search_from_node(word, self.trie)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)