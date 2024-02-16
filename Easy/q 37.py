"""
Given a linked list of N nodes. The task is to reverse this list.
"""

"""
# Node Class
class node:
    def __init__(self, val):
        self.data = val
        self.next = None
"""

class Solution:
    def reverseList(self, head):
        previous = None
        current = head
        
        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        
        head = previous
        return head
 
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

def printList(head):
    tmp = head
    while tmp:
        print(tmp.data, end=' ')
        tmp=tmp.next
    print()

if __name__=='__main__':
    for i in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]
        
        lis = Linked_List()
        for i in arr:
            lis.insert(i)
        
        newHead = Solution().reverseList(lis.head)
        printList(newHead)
