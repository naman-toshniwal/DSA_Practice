"""
Given a binary tree of size n, find its reverse level order traversal. ie- the traversal must begin from the last level.
"""

'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

from collections import deque
def reverseLevelOrder(root):
    ans = []
    q = deque()
    q.append(root)
    
    while not len(q) == 0:
        tmp = []
        sz = len(q)
        for i in range(sz):
            node = q.popleft()
            tmp.append(node.data)
            if node.left: q.append(node.left)
            if node.right : q.append(node.right)
        ans = tmp + ans   
    return ans

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
        ans = reverseLevelOrder(root)
        for i in ans:
            print(i,end=" ")
        print()
