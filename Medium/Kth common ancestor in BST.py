"""
Given a BST with n (n>=2) nodes, find the kth common ancestor of nodes x and y in the given tree. Return -1 if kth ancestor does not exists.

Nodes x and y will always be present in input BST, and x != y.
"""

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''

class Solution:
    def kthCommonAncestor(self, root, k, x, y):
        if x > y:
            x, y = y, x
        ancestors, node = [root.data], root
        
        while not (x <= node.data <= y):
            if x < node.data:
                node = node.left
            else:
                node = node.right
            ancestors.append(node.data)
        return ancestors[-k] if len(ancestors) >= k else -1

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
    k, x, y = map(int, input().split())
    if root is None:
        continue
    
    if root.left is None and root.right is None:
        continue
    
    ob = Solution()
    print(ob.kthCommonAncestor(root, k, x, y))
