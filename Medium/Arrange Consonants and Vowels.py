"""
Given a singly linked list having n nodes containing english alphabets ('a'-'z'). Rearrange the linked list in such a way that all the vowels come before the consonants while maintaining the order of their arrival. 
"""

"""
# Node Class

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

"""

class Solution:
    def arrangeCV(self, head):
        vow=['a','e','i','o','u']
        v=[]
        c=[]
        
        while head:
            if head.data in vow:
                v.append(head.data)
            else:
                c.append(head.data)
            head=head.next
       
        if len(v)>0:
            k=Node(v[0])
            head=k
            
            for i in v[1:]:
                k.next=Node(i)
                k=k.next
            
            for i in c:
                k.next=Node(i)
                k=k.next
       
        elif len(c)>0:
            k=Node(c[0])
            head=k
            for i in c[1:]:
                k.next=Node(i)
                k=k.next
                
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
        tmp = tmp.next
    print()

if __name__ == '__main__':
    for i in range(int(input())):
        n = int(input())
        arr = [str(x) for x in input().split()]

        lis = Linked_List()
        for i in arr:
            lis.insert(i)
        newHead = Solution().arrangeCV(lis.head)
        printList(newHead)
