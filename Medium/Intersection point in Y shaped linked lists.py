"""
Given two singly linked lists of size N and M, write a program to get the point where two linked lists intersect each other.
"""

'''
    Function to return the value at point of intersection
    in two linked list, connected in y shaped form.
    
    Function Arguments: head_a, head_b (heads of both the lists)
    
    Return Type: value in NODE present at the point of intersection
                 or -1 if no common point.

    {
        # Node Class
        class Node:
            def __init__(self, data):   # data -> value stored in node
                self.data = data
                self.next = None
    }
'''

def intersetPoint(head1,head2):
    l1 = head1
    l2 = head2
    
    while (l1 != l2):
        l1 = l1.next if l1 else head2
        l2 = l2.next if l2 else head1
    
    if l1 is None:
        return -1
    return l1.data

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
        temp=None
    
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            self.temp = self.head
            return
        else:
            self.temp.next = new_node
            self.temp = self.temp.next

if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        x,y,z = map(int,input().strip().split())
        a = LinkedList()
        b = LinkedList()
        nodes_a = list(map(int, input().strip().split()))
        nodes_b = list(map(int, input().strip().split()))
        nodes_common = list(map(int, input().strip().split()))

        for x in nodes_a:
            node=Node(x)
            a.append(node)  

        for x in nodes_b:
            node=Node(x)
            b.append(node)  

        for i in range(len(nodes_common)):
            node=Node(nodes_common[i])
            a.append(node)  

            if i== 0:
                b.append(node)
        
        print(intersetPoint(a.head,b.head))
