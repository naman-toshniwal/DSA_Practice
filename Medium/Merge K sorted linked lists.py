"""
Given K sorted linked lists of different sizes. The task is to merge them in such a way that after merging they will be a single sorted linked list.
"""

'''
    Your task is to merge the given k sorted
    linked lists into one list and return
    the the new formed linked list class.

    Function Arguments:
        arr is a list containing the n linkedlist head pointers
        n is an integer value
    
    node class:
    
class Node:
    def __init__(self,x):
        self.data = x
        self.next = None
'''

class Solution:
    def mergeKLists(self,arr,K):
        m = []
        for i in range(len(arr)):
            k = arr[i]
            while k:
                m.append(k.data)
                k = k.next
        
        m.sort()
        for i in m:
            print(i, end = " ")

class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def add(self,x):
        if self.head is None:
            self.head=Node(x)
            self.tail=self.head
        else:
            self.tail.next=Node(x)
            self.tail=self.tail.next
    
def printList(head):
    walk = head
    while walk:
        print(walk.data, end=' ')
        walk=walk.next
    print()

if __name__=="__main__":
    for _ in range(int(input())):
        n=int(input())
        line=[int(x) for x in input().strip().split()]
        heads=[]
        index=0
        
        for i in range(n):
            size=line[index]
            index+=1
            newList = LinkedList()
            
            for _ in range(size):
                newList.add(line[index])
                index+=1
            heads.append(newList.head)
        merged_list = Solution().mergeKLists(heads,n)
        printList(merged_list)
