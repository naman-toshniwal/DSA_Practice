"""
Given a binary tree with n nodes, find the number of pairs violating the BST property.
BST has the following properties:-

Every node is greater than its left child and less than its right child.
Every node is greater than the maximum value of in its left subtree and less than the minimum value in its right subtree.
The maximum in the left sub-tree must be less than the minimum in the right subtree.
"""

from typing import Optional
from collections import deque

"""
definition of binary tree node.
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def pairsViolatingBST(self, n, root):
        s = []
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            s.append(node.data)
            inorder(node.right)
        inorder(root)
        ans = 0
        
        def mergesort(arr):
            nonlocal ans
            
            if len(arr) <= 1:
                return arr
                
            mi = len(arr)//2
            a = mergesort(arr[:mi])
            b = mergesort(arr[mi:])
            i, j, ret = 0, 0, []
            
            while i < len(a) and j < len(b):
                if a[i] <= b[j]:
                    ret.append(a[i])
                    i += 1
                else:
                    ans += len(a)-i
                    ret.append(b[j])
                    j += 1
           
            if i < len(a):
                ret.extend(a[i:])
            
            if j < len(b):
                ret.extend(b[j:])
            return ret
        mergesort(s)
        return ans

class Node:
    def __init__(self,val):
        self.data=val
        self.right=None
        self.left=None

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
    treeString=input().strip()
    root = buildTree(treeString)
    return root
def inorder(root):
    if (root == None):
       return
    inorder(root.left);
    print(root.data,end=" ")
    inorder(root.right)

if __name__=="__main__":
    t = int(input())
    for _ in range(t):        
        n = int(input())        
        root = inputTree();        
        obj = Solution()
        res = obj.pairsViolatingBST(n, root)
        print(res)
