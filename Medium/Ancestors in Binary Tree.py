"""
Given a Binary Tree and an integer target. Find all the ancestors of the given target.

Note:

The ancestor of node x is node y, which is at the upper level of node x, and x is directly connected with node y. Consider multiple levels of ancestors to solve this problem.
In case there are no ancestors available, return an empty list.
"""

import sys
sys.setrecursionlimit(50000)
from collections import deque

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

def buildTree(s):
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def AncestorsUtil(self, root, target, nodes):
        if root == None:
            return False

        if root.data == target:
            return True

        if (self.AncestorsUtil(root.left, target, nodes)
                or self.AncestorsUtil(root.right, target, nodes)):
            nodes.append(root.data) 
            return True
        return False

    def Ancestors(self, root, target):
        nodes = []
        self.AncestorsUtil(root, target, nodes)
        return nodes

if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        target=int(input())
        nodes = Solution().Ancestors(root, target)
        for node in nodes:
            print(node,end=' ')
        print()
