"""
Given a binary search tree having n (n>1) nodes, the task is to find the minimum absolute difference between any two nodes.
"""

# class Node:
#     def __init__(self):
#         self.data = None
#         self.left = None
#         self.right = None
        
class Solution:
    def absolute_diff(self,root):
        arr=[]
        
        def inorder(node):
            if node.left:inorder(node.left)
            arr.append(node.data)
            if node.right:inorder(node.right)
        inorder(root)
        i=0
        j=i+1
        ans=float('inf')
        
        while j<len(arr):
            if arr[j]-arr[i]<ans:
                ans=arr[j]-arr[i]
            j+=1
            i+=1
        return ans

from collections import deque
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildTree(s):
    if (len(s) == 0 or s[0] == "N"):
        return None

    ip = list(map(str, s.split()))
    root = Node(int(ip[0]))
    size = 0
    q = deque()
    q.append(root)
    size = size + 1
    i = 1

    while size > 0 and i < len(ip):
        currNode = q[0]
        q.popleft()
        size = size - 1
        currVal = ip[i]

        if (currVal != "N"):
            currNode.left = Node(int(currVal))
            q.append(currNode.left)
            size = size + 1
        i = i + 1

        if (i >= len(ip)):
            break
        currVal = ip[i]

        if (currVal != "N"):
            currNode.right = Node(int(currVal))
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root

for _ in range(int(input())):
    s = input()
    root = buildTree(s)
    if root is None:
        continue
    if root.left is None and root.right is None:
        continue
    
    ob = Solution()
    print(ob.absolute_diff(root))
