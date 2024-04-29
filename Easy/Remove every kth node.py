"""
Given a singly linked list having n nodes, your task is to remove every kth node from the linked list. 
"""

'''
class node:
    def __init__(self,x):
        self.data = x
        self.next = None
'''

class Solution:
    def deleteK(self, head, k):
        dummy=node(0)
        dummy.next=head
        prev,curr=dummy,head
        count=0
        
        while curr:
            count+=1
            if count%k==0:
                prev.next=curr.next
            else:
                prev=curr
            curr=curr.next
        return dummy.next

class node:
    def __init__(self, x):
        self.data = x
        self.next = None

def createLinkedList(arr):
    head = node(arr[0])
    curr = head
    for i in range(1, len(arr)):
        new_node = node(arr[i])
        curr.next = new_node
        curr = curr.next
    return head

def printlist(ptr):
    while ptr != None:
        print(ptr.data, end=" ")
        ptr = ptr.next
    print()

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())

        obj = Solution()
        head = createLinkedList(arr)
        new_head = obj.deleteK(head, k)
        printlist(new_head)
