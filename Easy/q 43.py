"""
Given a binary tree, find if it is height balanced or not. 
A tree is height balanced if difference between heights of left and right subtrees is not more than one for all nodes of tree. 

A height balanced tree
        1
     /     \
   10      39
  /
5

An unbalanced tree
        1
     /    
   10   
  /
5
"""

'''class Node: 
    # Constructor to create a new Node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None'''

class Solution:
    def height(self, root):
        if root == None:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1
        
    def isBalanced(self,root):
        if root == None:
            return True
        
        if (abs(self.height(root.left) - self.height(root.right)) <= 1) and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False

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
        ob = Solution()
        if ob.isBalanced(root):
            print(1) 
        else:
            print(0)
