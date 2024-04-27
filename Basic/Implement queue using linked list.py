"""
Implement a Queue using Linked List. 
A Query Q is of 2 Types
(i) 1 x   (a query of this type means  pushing 'x' into the queue)
(ii) 2     (a query of this type means to pop an element from the queue and print the poped element)
"""

class MyStack:
    def __init__(self):
        self.root=None
    
    def isEmpty(self):
        return self.root is None

    def push(self, data):
        newnode=StackNode(data)
        newnode.next=self.root
        self.root=newnode

    def pop(self):
        if self.isEmpty():
            return -1
        
        temp=self.root
        self.root=self.root.next
        popped=temp.data
        return popped

class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = MyStack()
        q = int(input())
        q1 = list(map(int, input().split()))
        i = 0
        while(i < len(q1)):
            if(q1[i] == 1):
                s.push(q1[i + 1])
                i = i + 2
            elif(q1[i] == 2):
                print(s.pop(), end=" ")
                i = i + 1
            elif(s.isEmpty()):
                print(-1)
        print()
