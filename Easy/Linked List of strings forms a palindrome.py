"""
Given a linked list with string data, check whether the combined string formed is palindrome. If the combined string is palindrome then return true otherwise return false.
"""

'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''

def compute(head): 
    s = ""
    curr = head
    while curr:
        s += curr.data
        curr = curr.next
    return s == s[::-1]
    
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

if __name__ == '__main__':
    t = int(input())
    for tcs in range(t):
        n1 = int(input())
        arr1 = input().split()
        ll1 = Llist()
        tail = None
        for nodeData in arr1:
            tail = ll1.insert(nodeData, tail)

        if compute(ll1.head):
            print('true')
        else:
            print('false')
