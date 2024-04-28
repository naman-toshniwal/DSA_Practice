"""
Given a singly linked list, delete middle of the linked list. For example, if given linked list is 1->2->3->4->5 then linked list should be modified to 1->2->4->5.
If there are even nodes, then there would be two middle nodes, we need to delete the second middle element. For example, if given linked list is 1->2->3->4->5->6 then it should be modified to 1->2->3->5->6.
If the input linked list has single node, then it should return NULL.
"""

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def deleteMid(self,head):
        if head == None or head.next == None:
             return None
        curr = head
        count = 0
        
        while curr != None:
            count += 1
            curr = curr.next
        curr = head
        
        for i in range((count // 2)-1):
            curr = curr.next
        temp = curr.next.next   
        curr.next = temp
        return head

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Llist:
    def __init__(self):
        self.head = None

    def insert(self, data, tail):
        node = Node(data)

        if not self.head:
            self.head = node
            return node

        tail.next = node
        return node

def printList(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

if __name__ == '__main__':
    t = int(input())

    for tcs in range(t):
        n=int(input())
        arr1 = [int(x) for x in input().split()]
        ll = Llist()
        tail = None
        for nodeData in arr1:
            tail = ll.insert(nodeData, tail)
        obj = Solution();
        res=obj.deleteMid(ll.head)
        printList(res)
