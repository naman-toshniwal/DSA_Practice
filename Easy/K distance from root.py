"""
Given a binary tree having n nodes and an integer k. Print all nodes that are at distance k from the root (root is considered at distance 0 from itself). Nodes should be printed from left to right.
"""

'''
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def KDistance(self, root, k):
        result = []
        self.findKDistanceNodes(root, k, result)
        return result

    def findKDistanceNodes(self, node, k, result):
        if not node:
            return
        
        if k == 0:
            result.append(node.data)
            return
        self.findKDistanceNodes(node.left, k - 1, result)
        self.findKDistanceNodes(node.right, k - 1, result)

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
        k = int(input())
        s=input()
        root=buildTree(s)
        ob=Solution();
        nodes = ob.KDistance(root,k)
        for node in nodes:
            print(node,end=' ')
        print()
