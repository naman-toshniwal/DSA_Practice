"""
Given two sorted linked lists consisting of N and M nodes respectively. The task is to merge both of the list (in-place) and return head of the merged list.
"""

'''
    Function to merge two sorted lists in one
    using constant space.
    
    Function Arguments: head_a and head_b (head reference of both the sorted lists)
    Return Type: head of the obtained list after merger.

    {
        # Node Class
        class Node:
            def __init__(self, data):   # data -> value stored in node
                self.data = data
                self.next = None
    }
'''

def sortedMerge(head1, head2):
    randNode = Node(-1)
    ptr = randNode
    cur1 = head1
    cur2 = head2
    
    while cur1 and cur2:
        if cur1.data<cur2.data:
            ptr.next = cur1
            cur1 = cur1.next
        else:
            ptr.next = cur2
            cur2 = cur2.next
        ptr = ptr.next
    
    if cur1:
        ptr.next= cur1
    elif cur2:
        ptr.next = cur2
    return randNode.next

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

def printList(n):
    while n is not None:
        print(n.data, end=' ')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        n,m = map(int, input().strip().split())
        a = LinkedList() 
        b = LinkedList() 
        nodes_a = list(map(int, input().strip().split()))
        nodes_b = list(map(int, input().strip().split()))
        
        for x in nodes_a:
            a.append(x)
        
        for x in nodes_b:
            b.append(x)
        printList(sortedMerge(a.head,b.head))
