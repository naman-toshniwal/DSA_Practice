"""
Given a linked list consisting of L nodes and given a number N. The task is to find the Nth node from the end of the linked list.
"""

'''
    Your task is to return the data stored in
    the nth node from end of linked list.
    
    Function Arguments: head (reference to head of the list), n (pos of node from end)
    Return Type: Integer or -1 if no such node exits.

    {
        # Node Class
        class Node:
            def __init__(self, data):   # data -> value stored in node
                self.data = data
                self.next = None
    }
'''

def getNthFromLast(head,n):
    currentNode = head
    nthNode = head
    
    while n:
        if n and currentNode == None:
            return -1
        currentNode = currentNode.next
        n -= 1
        
    while currentNode:
        currentNode = currentNode.next
        nthNode = nthNode.next
    return nthNode.data

import atexit
import io
import sys

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
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n,nth_node = map(int, input().strip().split())
        a = LinkedList() 
        nodes_a = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)  
        print(getNthFromLast(a.head,nth_node))
