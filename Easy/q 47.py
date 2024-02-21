"""
Given a Binary Search Tree (with all values unique) and two node values n1 and n2 (n1!=n2). Find the Lowest Common Ancestors of the two nodes in the BST.
"""

def LCA(root, n1, n2):
    while root:
        if root.data < n1 and root.data < n2:
            root = root.right
        elif root.data > n1 and root.data > n2:
            root = root.left
        else:
            break
    return root

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
        n1,n2=list(map(int,input().split()))
        print(LCA(root,n1,n2).data);
