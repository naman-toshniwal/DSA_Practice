"""
Given a binary tree with n nodes. Find the zig-zag level order traversal of the binary tree.
"""

'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

from collections import deque
class Solution:
    def zigZagTraversal(self, root):
        result, left_to_right, queue = [root.data], True, deque([root])
        
        while queue:
            temp_queue, level_values = deque(), []
            
            for node in queue:
                if node.left:
                    temp_queue.append(node.left)
                    level_values.append(node.left.data)
                
                if node.right:
                    temp_queue.append(node.right)
                    level_values.append(node.right.data)
            
            result.extend(level_values[::-1] if left_to_right else level_values)
            queue, left_to_right = temp_queue, not left_to_right
            
        return result

from collections import defaultdict
from collections import deque

class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
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
    
if __name__ == '__main__':
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        ob = Solution()
        res = ob.zigZagTraversal(root)
        for i in range (len (res)):
            print (res[i], end = " ")
        print()
