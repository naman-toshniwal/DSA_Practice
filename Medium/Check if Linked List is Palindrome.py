"""
Given a singly linked list of size N of integers. The task is to check if the given linked list is palindrome or not.
"""

'''
    Your task is to check if given linkedlist
    is a pallindrome or not.
    
    Function Arguments: head (reference to head of the linked list)
    Return Type: boolean , no need to print just return True or False.

    {
        # Node Class
        class Node:
            def __init__(self, data):   # data -> value stored in node
                self.data = data
                self.next = None
    }
'''

class Solution:
    def reverse(self, head):
        prev = None
        curr = head
        
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev
    
    def isPalindrome(self, head):
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        rev = self.reverse(slow)
        
        while rev:
            if head.data != rev.data:
                return False
            head = head.next
            rev = rev.next
        return True

import atexit
import io
import sys

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
        n = int(input())
        a = LinkedList() 
        nodes_a = list(map(int, input().strip().split()))

        for x in nodes_a:
            a.append(x)  

        if Solution().isPalindrome(a.head):
            print(1)
        else:
            print(0)
