"""
Given the head of a linked list, determine whether the list contains a loop. If a loop is present, return the number of nodes in the loop, otherwise return 0.
"""

'''
Structure of node

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    def countNodesInLoop(self, head):
        if not head:
            return 0
        s,f=head,head
        flag=0
        
        while f and f.next:
            s=s.next
            f=f.next.next
            
            if s==f:
                flag=1
                s=s.next
                count=1
                
                while s!=f:
                    s=s.next
                    count+=1
                break
            
        return count if flag else 0

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_list(node):
    while node:
        print(node.data, end=' ')
        node = node.next
    print()

def loop_here(head, pos):
    if pos == 0:
        return

    walk = head
    for _ in range(1, pos):
        walk = walk.next

    tail = head
    while tail.next:
        tail = tail.next

    tail.next = walk

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split('\n')
    t = int(data[0])
    index = 1
    for _ in range(t):
        arr = list(map(int, data[index].split()))
        k = int(data[index + 1])
        head = Node(arr[0])
        tail = head
        for value in arr[1:]:
            tail.next = Node(value)
            tail = tail.next
        loop_here(head, k)
        ob = Solution()
        res = ob.countNodesInLoop(head)
        print(res)
        index += 2
