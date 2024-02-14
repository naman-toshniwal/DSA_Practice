"""
Given a linked list of N nodes. The task is to check if the linked list has a loop. Linked list can contain self loop.
"""

'''
        # Node Class
        class Node:
            def __init__(self, data):   # data -> value stored in node
                self.data = data
                self.next = None
    
'''
class Solution:
    def detectLoop(self, head):
        while (head != None):
            if head.data == 0:
                return True
            head.data = 0
            
            head = head.next
        return False

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
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

    def loopHere(self,pos):
        if pos==0:
            return        
        walk = self.head

        for i in range(1,pos):
            walk = walk.next        
        self.tail.next = walk

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        LL = LinkedList()

        for i in input().split():
            LL.insert(int(i))
        LL.loopHere(int(input()))        
        print(Solution().detectLoop(LL.head))
