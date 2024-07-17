"""
Given an array parent that is used to represent a tree. The array indices (0-based indexing) are the values of the tree nodes and parent[i] denotes the parent node of a particular node. The parent of the root node would always be -1, as there is no parent for the root. Construct the standard linked representation of Binary Tree from this array representation and return the root node of the constructed tree.

Note: If two elements have the same parent, the one that appears first in the array will be the left child and the other is the right child. You don't need to print anything, the driver code will print the level order traversal of the returned root node to verify the output.
"""

'''
# A node structure
class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
'''

class Solution:
    def createTree(self, parent):
        temp = {}

        for key, parent_index in enumerate(parent):
            node = temp[parent_index] = temp.get(parent_index, Node(parent_index))
            
            if not node.left:
                node.left = temp[key] = temp.get(key, Node(key))
            else:
                node.right = temp[key] = temp.get(key, Node(key))

        return temp[-1].left

import atexit
import io
import sys
from collections import defaultdict

'''
_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
'''

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def traverse_level_order(root):
    if root is None:
        return
    que = []
    que.append(root)
    while 1:
        n = len(que)
        if n == 0:
            break
        sorted_nodes = [node.key for node in que]
        sorted_nodes.sort()
        print(*sorted_nodes, end=" ")
        while (n > 0):
            node = que.pop(0)
            if node.left != None:
                que.append(node.left)
            if node.right != None:
                que.append(node.right)
            n -= 1

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())  # number of nodes in tree
        a = list(map(int,
                     input().strip().split()))  # parent child info in list
        ob = Solution()
        traverse_level_order(ob.createTree(a))
        print()
