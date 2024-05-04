"""
Given inorder and postorder traversals of a binary tree(having n nodes) in the arrays in[] and post[] respectively. The task is to construct a binary tree from these traversals.

Driver code will print the preorder traversal of the constructed tree.
"""

'''
class Node:
            def __init__(self, data):
                self.data = data
                self.left = self.right = None
'''

class Solution:
    def buildTree(self,In, post, n):
        if len(In):
            node = Node(post.pop())
            ind = In.index(node.data)
            node.right = self.buildTree(In[ind + 1:],post,n)
            node.left = self.buildTree(In[:ind],post,n)
            return node
        
        else:
            return None

import atexit
import io
import sys
from collections import  defaultdict

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER
@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def preOrder(node):
    if node == None:
        return
    print(node.data, end=" ")
    preOrder(node.left)
    preOrder(node.right)
    
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input()) 
        in_order = list(map(int, input().strip().split()))  
        post_order = list(map(int, input().strip().split()))  
        ob = Solution()
        preOrder(ob.buildTree(in_order,post_order,n))
        print()
