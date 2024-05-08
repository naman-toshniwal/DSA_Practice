"""
Given a Binary Tree of nodes, you need to find all the possible paths from the root node to all the leaf nodes of the binary tree.
"""

from typing import Optional
from collections import deque
from typing import List

"""
definition of binary tree node.
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def Paths(self, root : Optional['Node']) -> List[List[int]]:
        res = []
        
        def dfs(root, sub):
            if not root:
                return
            sub.append(root.data)
            
            if not root.left and not root.right:
                res.append(sub.copy())
                return
            dfs(root.left, sub.copy())
            dfs(root.right, sub.copy())
        
        dfs(root, [])
        return res

class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None

def buildTree(s):
    if(len(s)==0 or s[0]=="N"):           
        return None

    ip=list(map(str,s.split()))
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    q.append(root)                            
    size=size+1 
    i=1                                       
    while(size>0 and i<len(ip)):
        currNode=q[0]
        q.popleft()
        size=size-1
        currVal=ip[i]
        
        if(currVal!="N"):
            currNode.left=Node(int(currVal))
            q.append(currNode.left)
            size=size+1
        i=i+1

        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        if(currVal!="N"):
            currNode.right=Node(int(currVal))
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root

def inputTree():
    treeString = input().strip()
    root = buildTree(treeString)
    return root

def inorder(root):
    if (root == None):
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

class IntMatrix:

    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        root = inputTree()
        obj = Solution()
        res = obj.Paths(root)
        IntMatrix().Print(res)
