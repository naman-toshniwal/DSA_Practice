"""
Given the two singly Linked Lists respectively. The task is to check whether two linked lists are identical or not. 
Two Linked Lists are identical when they have the same data and with the same arrangement too. If both Linked Lists are identical then return true otherwise return false. 
"""

'''
# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None
        
'''

def areIdentical(head1, head2):
    while head1 and head2:
        if head1.data == head2.data:
            head1 = head1.next
            head2 = head2.next
        else:
            return False
    
    if head1 is None and head2 is None:
        return True
    return False

class node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self, val):
        new_node = node(val)
        new_node.data = val
        new_node.next = self.head
        self.head = new_node

def printList(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

def createList(arr, n):
    lis = Linked_List()
    for i in range(n):
        lis.insert(arr[i])
    return lis.head

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        head1 = createList(arr, n)
        n = int(input())
        arr = list(map(int, input().strip().split()))
        head2 = createList(arr, n)
        if (areIdentical(head1, head2)):
            print('true')
        else:
            print('false')
