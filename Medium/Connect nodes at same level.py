"""
Given a binary tree, connect the nodes that are at same level. You'll be given an addition nextRight pointer for the same.

Initially, all the nextRight pointers point to garbage values. Your function should set these pointers to point next right for each node.
       10                       10 ------> NULL
      / \                       /      \
     3   5       =>     3 ------> 5 --------> NULL
    / \     \               /  \           \
   4   1   2          4 --> 1 -----> 2 -------> NULL
"""

import sys
sys.setrecursionlimit(50000)

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        self.nextRight = None
        
class Solution:
    def connect(self, root):
        if not root:
            return root
        s=[root]
        
        while s:
            prev=None
            n=len(s)
            
            for i in range(n):
                curr=s.pop(0)
                
                if prev is not None:
                    prev.nextRight=curr
                prev=curr
                
                if curr.left:
                    s.append(curr.left)
                
                if curr.right:
                    s.append(curr.right)
                
            prev=None
        return root

import sys
sys.setrecursionlimit(50000)
from collections import deque

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        self.nextRight = None
    
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

def InOrder(root):
    '''
    :param root: root of the given tree.
    :return: None, print the space separated in order Traversal of the given tree.
    '''
    if root is None: 
        return
    InOrder(root.left) 
    print(root.data, end=" ") 
    InOrder(root.right) 

def printSpecial(root):
    if root==None:
        return 
    next_root=None
    while root!=None:
        print(root.data,end=" ")
        if root.left and not next_root:
            next_root=root.left
        elif root.right and not next_root:
            next_root=root.right
        root=root.nextRight
    printSpecial(next_root)
 
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        obj = Solution();
        obj.connect(root)
        printSpecial(root)
        print()
        InOrder(root)
        print()
