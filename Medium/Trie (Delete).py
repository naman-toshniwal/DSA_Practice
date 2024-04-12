"""
Trie is an efficient information retrieval data structure. This data structure is used to store Strings and search strings, String stored can also be deleted. Given a Trie root for a larger string super and a string key, delete all the occurences of key in the Trie.
"""

class Solution():
    def deleteKey(self, root, key):
        n = len(key)
        
        for i in range(n):
            index = charToIndex(key[i])
            if root.children[index]:
                root = root.children[index]
            else:
                return
        
        root.isEndOfWord = False

class TrieNode: 
    def __init__(self): 
        self.children = [None]*26
        self.isEndOfWord = False
  
class Trie: 
    def __init__(self): 
        self.root =TrieNode()
        
def charToIndex(ch):
    return ord(ch)-ord('a')
  
def insert(root,key):
    for e in key:
        idx=charToIndex(e)
    
        if not root.children[idx]:
            root.children[idx]=TrieNode()
        root=root.children[idx]  
    root.isEndOfWord=True

def search(root, key):
    for e in key:
        idx=charToIndex(e)
        
        if not root.children[idx]:
            return
        root=root.children[idx]
    return root.isEndOfWord

if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=input().strip().split()
        key=input()
        
        t=Trie()
        
        for s in arr:
            insert(t.root,s)
        
        Solution().deleteKey(t.root, key)

        if search(t.root, key):
            print(0)
        else:
            print(1)
