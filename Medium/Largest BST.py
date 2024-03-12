"""
Given a binary tree. Find the size of its largest subtree that is a Binary Search Tree.
Note: Here Size is equal to the number of nodes in the subtree.
"""

class Solution:
    def  __init__(self):
        self.count = 0
        self.l = 0
        
    def heightBST(self, root):
        if root.left:
            self.heightBST(root.left)
        self.l += 1
        
        if root.right:
            self.heightBST(root.right)
            
    def findBST(self, root, minn, maxx):
        if not root:
            return True
        
        if root.data <= minn or root.data >= maxx:
            return False
        
        return self.findBST(root.left, minn, root.data) and self.findBST(root.right, root.data, maxx)
        
    def inOrder(self, root):
        if root.left:
            self.inOrder(root.left)
        
        if root.right:
            self.inOrder(root.right)
        
        if self.findBST(root, float('-inf'), float('inf')):
            self.heightBST(root)
            self.count = max(self.count, self.l)
            self.l = 0
        
    def largestBst(self, root):
        if not root:
            return 0
        
        ans = float('-inf')
        self.inOrder(root)
        return self.count

import sys
sys.setrecursionlimit(1000000)
from collections import deque

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

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

if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()

        root = buildTree(s)
        ob = Solution()
        print(ob.largestBst(root))
