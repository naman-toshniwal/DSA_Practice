"""
Given two decimal numbers, num1 and num2, represented by linked lists of size n and m respectively. The task is to return a linked list that represents the sum of these two numbers.

For example, the number 190 will be represented by the linked list, 1->9->0->null, similarly 25 by 2->5->null. Sum of these two numbers is 190 + 25 = 215, which will be represented by 2->1->5->null. You are required to return the head of the linked list 2->1->5->null.

Note: There can be leading zeros in the input lists, but there should not be any leading zeros in the output list.
"""

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def addTwoLists(self, num1, num2):
        list1=""
        list2=""
        
        while num1:
            list1=list1+str(num1.data)
            num1=num1.next
            
        while num2:
            list2=list2+str(num2.data)
            num2=num2.next
            
        res=int(list1)+int(list2)
        t=str(res)       
        new=LinkedList()
        
        for i in range(len(t)):
            new.insert(int(t[i]))
        return new.head

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

def printList(n):
    while n:
        print(n.data,end=' ')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        arr1 = ( int(x) for x in input().split() )
        num1 = LinkedList()

        for i in arr1:
            num1.insert(i)
        
        m = int(input())
        arr2 = ( int(x) for x in input().split() )
        num2 = LinkedList()

        for i in arr2:
            num2.insert(i)
        
        res = Solution().addTwoLists(num1.head, num2.head)
        printList(res)
