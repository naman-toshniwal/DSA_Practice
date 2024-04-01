"""
Given the root of a binary search tree and a number n, find the greatest number in the binary search tree that is less than or equal to n. 
"""

'''
class Node:
    """ Class Node """
    def __init__(self, value):
        self.left = None
        self.key = value
        self.right = None
'''

from collections import deque
class Solution:
    def findMaxForN(self, root, n):
        if not root:
            return -1
        lis = []
        q = deque([root])
        
        while q:
            siz = len(q)
            level = []
            
            for i in range(siz):
                node = q.popleft()
                level.append(node.key)
                
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            lis.extend(level)
        ans = 0
       
        for i in lis:
            if i > ans and i<=n:
                ans = i
        
        if ans:
            return ans
        return -1

from collections import deque
class Node:
    def __init__(self, val):
        self.right = None
        self.key = val
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

    while (size > 0 and i < len(ip)):
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
        n = int(input())
        ob = Solution()
        print(ob.findMaxForN(root, n))
