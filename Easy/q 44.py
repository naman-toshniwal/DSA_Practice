"""
Given a Binary Tree, return Left view of it. Left view of a Binary Tree is set of nodes visible when tree is visited from Left side. The task is to complete the function leftView(), which accepts root of the tree as argument. If no left view is possible, return an empty tree.

Left view of following tree is 1 2 4 8.

          1
       /     \
     2        3
   /     \    /    \
  4     5   6    7
   \
     8   
"""

'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

def LeftView(root):
    if root is None:
        return []
    queue = [root]
    output = []
    
    while queue:
        length = len(queue)
        output.append(queue[0].data)
        
        for i in range(length):
            temp = queue.pop(0)
            
            if temp.left:
                queue.append(temp.left)
            
            if temp.right:
                queue.append(temp.right)
    
    return output

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
        result = LeftView(root)
        for value in result:
            print(value,end=" ")
        print()
