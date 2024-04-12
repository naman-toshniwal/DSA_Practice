"""
Complete the Insert and Search functions for a Trie Data Structure. 

Insert: Accepts the Trie's root and a string, modifies the root in-place, and returns nothing.
Search: Takes the Trie's root and a string, returns true if the string is in the Trie, otherwise false.
Note: To test the correctness of your code, the code-judge will be inserting a list of N strings called into the Trie, and then will search for the string key in the Trie. The code-judge will generate 1 if the key is present in the Trie, else 0.
"""

"""
class TrieNode: 
    def __init__(self): 
        self.children = [None]*26
        # isEndOfWord is True if node represent the end of the word 
        self.isEndOfWord = False
"""

class Solution:
    def insert(self, root, key):
        for e in key:
            ind=ord(e)-ord("a")
            
            if root.children[ind] is None:
                root.children[ind]=TrieNode()
            root=root.children[ind]
        root.isEndOfWord=True

    def search(self, root, key):
        for e in key:
            ind=ord(e)-ord("a")
            
            if root.children[ind] is None:
                return False
            root=root.children[ind]
        return root.isEndOfWord

class TrieNode: 
    def __init__(self): 
        self.children = [None]*26
        self.isEndOfWord = False
  
class Trie: 
    def __init__(self): 
        self.root =TrieNode()
        
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=input().strip().split()
        strs=input()
        
        t=Trie()
        ob = Solution()
        
        for s in arr:
            ob.insert(t.root,s)
        
        if ob.search(t.root,strs):
            print(1)
        else:
            print(0)
