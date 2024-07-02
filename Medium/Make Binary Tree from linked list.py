"""
Given a Linked List Representation of Complete Binary Tree. Your task is to construct the Binary tree from the given linkedlist and return the root of the tree.
The result will be judged by printing the level order traversal of the Binary tree. 
Note: The complete binary tree is represented as a linked list in a way where if the root node is stored at position i, its left, and right children are stored at position 2*i+1, and 2*i+2 respectively. H is the height of the tree and this space is used implicitly for the recursion stack.
"""

'''
class ListNode:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.next = None

# Tree Node structure
class Tree:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

'''

def convert(head):
    a = []
    curr = head
    n=0
    
    while curr!=None:
        a.append(curr.data)
        curr = curr.next
        n += 1
        
    def buildTree(i):
        if i>=n:
            return
        newNode = Tree(a[i])
        left = buildTree(2*i+1)
        right = buildTree(2*i+2)
        newNode.left = left
        newNode.right = right
        return newNode
        
    root = buildTree(0)
    return root

import atexit
import io
import sys

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Conversion:
    def __init__(self, data=None):
        self.head = None
        self.root = None

    def push(self, new_data):
        new_node = ListNode(new_data)
        new_node.next = self.head
        self.head = new_node

    def levelorderTraversal(self, root):
        mylist = []  # reverse list of nodes
        if root is None:
            return
        que = []
        que.append(root)
        while True:
            n = len(que)
            if n == 0:
                break
            while (n > 0):
                node = que.pop(0)
                mylist.append(node.data)
                if node.left is not None:
                    que.append(node.left)
                if node.right is not None:
                    que.append(node.right)
                n -= 1
        mylist = mylist[::-1]
        print(*mylist)
        return

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int, input().strip().split()))
        mylist = Conversion()  # Create Linked List to be used
        for i in range(n):
            mylist.push(a[i])  # push elements in linked list
        # convert the linked list to binary tree
        root = convert(mylist.head)
        mylist.levelorderTraversal(root)
