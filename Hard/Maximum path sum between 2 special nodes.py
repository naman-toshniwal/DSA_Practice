"""
Given a binary tree in which each node element contains a number. Find the maximum possible path sum from one special node to another special node.

Note: Here special node is a node which is connected to exactly one different node.
"""

class Solution:        
    def __init__(self):
        self.res = -1*(2**63 - 1)
    
    def s(self, root, ischild):
        if root is None:
            return 0
    
        if root.left is None and root.right is None:
            return root.data
        
        l = self.s(root.left, True)
        r = self.s(root.right, True)
        temp = root.data+l+r
    
        if root.left is None:
            l = -1*(2**63 - 1)
    
        if root.right is None:
            r = -1*(2**63 - 1)
        ans = max(l,r) + root.data
        
        if root.left is not None and root.right is not None or ischild == False:
            self.res = max(self.res,  temp)
        return ans
        
    def maxPathSum(self, root):
        self.s(root, False)
        return self.res


from collections import deque
import sys
sys.setrecursionlimit(10**6)  

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
        print(ob.maxPathSum(root))
