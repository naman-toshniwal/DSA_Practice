"""
Given two BSTs, return elements of both BSTs in sorted form.
"""

from collections import deque
class Node:
    """ Class Node """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
 
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

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    def merge(self, root1, root2):
        stack1,stack2 = [root1],[root2]
        res =[]
        curr1,curr2 = root1,root2
        
        while stack1 or stack2:
            while curr1.left:
                stack1.append(curr1.left)
                curr1 = curr1.left
        
            while curr2.left:
                stack2.append(curr2.left)
                curr2 = curr2.left
        
            if (not stack1) or (stack2 and stack1[-1].data >= stack2[-1].data):
                node = stack2.pop()
                res.append(node.data)
                if node.right:
                    stack2.append(node.right)
                    curr2 = node.right
        
            else:
                node = stack1.pop()
                res.append(node.data)
                if node.right:
                    stack1.append(node.right)
                    curr1 = node.right

        return res

if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s1=input()
        s2=input()
        root1=buildTree(s1)
        root2=buildTree(s2)
        res = Solution().merge(root1,root2)
        for i in range (len(res)):
            print (res[i], end = " ")
        print()
