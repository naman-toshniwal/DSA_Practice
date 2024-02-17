"""
Given a linked list of N nodes where nodes can contain values 0s, 1s, and 2s only. The task is to segregate 0s, 1s, and 2s linked list such that all zeros segregate to head side, 2s at the end of the linked list, and 1s in the mid of 0s and 2s.
"""

'''
    Your task is to segregate the list of 
    0s,1s and 2s.
    
    Function Arguments: head of the original list.
    Return Type: head of the new list formed.

    {
        # Node Class
        class Node:
            def __init__(self, data):   # data -> value stored in node
                self.data = data
                self.next = None
    }

'''

class Solution:
    def segregate(self, head):
        arr = []
        current = head
        
        while current:
            arr.append(current.data)
            current = current.next
        
        sorted_arr = sorted(arr)
        new_head = Node(sorted_arr[0])
        current = new_head
        
        for data in sorted_arr[1:]:
            current.next = Node(data)
            current = current.next
        return new_head

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

def printList(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data,end=" ")
        curr_node=curr_node.next
    print()

if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n = int(input())
        a = LinkedList() # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)  
        printList(Solution().segregate(a.head))
