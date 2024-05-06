"""
Given a Binary Tree of n nodes, find all the nodes that don't have any siblings. You need to return a list of integers containing all the nodes that don't have a sibling in sorted order (Increasing).

Two nodes are said to be siblings if they are present at the same level, and their parents are the same.

Note: The root node can not have a sibling so it cannot be included in our answer.
"""

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

def help(root,ans):
    if root is None:
        return
    
    if root.left is not None and root.right is None:
        ans.append(root.left.data)
    
    if root.left is None and root.right is not None:
        ans.append(root.right.data)
    help(root.left,ans)
    help(root.right,ans)

def noSibling(root):
    ans=[]
    help(root,ans)
    return [-1] if ans==[] else sorted(ans)

from collections import deque
class Node:
   def __init__(self, val):
        self.right = None
        self.data = val
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

if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        ans = noSibling(root)
        for i in ans:
            print(i,end=" ")
        print()
