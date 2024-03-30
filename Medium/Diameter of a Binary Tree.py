"""
The diameter of a tree (sometimes called the width) is the number of nodes on the longest path between two end nodes. The diagram below shows two trees each with diameter nine, the leaves that form the ends of the longest path are shaded (note that there is more than one path in each tree of length nine, but no path longer than nine nodes). 
"""

class Solution:
    def diameterInternal(self,root):
        if root == None:
            return 0, 0
        
        l_dia, l_height = self.diameterInternal(root.left)
        r_dia, r_height = self.diameterInternal(root.right)
        d = l_height + r_height + 1
        D = max(l_dia, r_dia, d)
        
        if l_height >= r_height:
            H = l_height + 1
        else:
            H = r_height + 1
        return D, H
    
    def diameter(self,root):
        dia, height = self.diameterInternal(root)
        return dia

from collections import deque
import sys
sys.setrecursionlimit(50000)

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
        k=Solution().diameter(root)
        print(k)
