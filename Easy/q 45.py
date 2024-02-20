"""
Given a binary tree, find its height.
"""

'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def height(self, root):
        if root is None:
            return 0
        else:
            left = self.height(root.left)
            right = self.height(root.right)
            return max(left, right) + 1

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
        print(ob.height(root))
