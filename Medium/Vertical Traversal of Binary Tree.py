"""
Given a Binary Tree, find the vertical traversal of it starting from the leftmost level to the rightmost level.
If there are multiple nodes passing through a vertical line, then they should be printed as they appear in level order traversal of the tree.
"""

from collections import OrderedDict
class Solution:
    def verticalOrder(self, root): 
        odict=OrderedDict()
        queue=[[root,0,0]]
        
        while queue:
            a=queue.pop(0) 
            node=a[0] 
            vertical=a[1] 
            level=a[2] 
            
            if vertical not in odict: 
                odict[vertical]=[[level,node.data]]
            else:
                odict[vertical].append([level,node.data])
            
            if node.left:
                queue.append([node.left,vertical-1,level+1])
            
            if node.right:
                queue.append([node.right,vertical+1,level+1])
        sorted_dict=sorted(odict.items(),key=lambda x:x[0]) 
        result=[] 
       
        for i in sorted_dict:
            for j in i[1]:
                result.append(j[1])
        return result

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
    import sys
    sys.setrecursionlimit(10000)
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        res = Solution().verticalOrder(root)
        for i in res:
            print (i, end=" ")
        print()
