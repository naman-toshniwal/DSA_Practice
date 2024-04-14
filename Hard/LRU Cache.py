"""
Design a data structure that works like a LRU Cache. Here cap denotes the capacity of the cache and Q denotes the number of queries. Query can be of two types:

SET x y: sets the value of the key x with value y
GET x: gets the key of x if present else returns -1.

The LRUCache class has two methods get() and set() which are defined as follows.

get(key): returns the value of the key if it already exists in the cache otherwise returns -1.
set(key, value): if the key is already present, update its value. If not present, add the key-value pair to the cache. If the cache reaches its capacity it should invalidate the least recently used item before inserting the new item.
In the constructor of the class the capacity of the cache should be initialized.
"""

class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=self.prev=None

class LRUCache:
    hsmap=dict()
    capacity=0
    count=0
    head=tail=None
  
    def __init__(self,cap):
        self.hsmap=dict()
        self.capacity=cap
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail
        self.head.prev=None
        self.tail.prev=self.head
        self.tail.next=None
        count=0

    def addToHead(self,node):
        node.next=self.head.next
        node.next.prev=node
        node.prev=self.head
        self.head.next=node

    def deleteNode(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev

    def get(self, key):
        if key in self.hsmap:
            node=self.hsmap[key]
            res=node.value
            self.deleteNode(node)
            self.addToHead(node)
            return res
        return -1

    def set(self, key, value):
        if key in self.hsmap:
            node=self.hsmap[key]
            node.value=value
            self.deleteNode(node)
            self.addToHead(node)
        else:
            node=Node(key,value)
            self.hsmap[key]=node

            if self.count<self.capacity:
                self.count+=1
                self.addToHead(node)
            else:
                self.hsmap.pop(self.tail.prev.key)
                self.deleteNode(self.tail.prev)
                self.addToHead(node)

if __name__ == '__main__':
    test_cases = int(input())

    for cases in range(test_cases):
        cap = int(input())  
        qry=int(input())  
        a = list(map(str, input().strip().split()))        
        lru=LRUCache(cap)
        i=0
        q=1

        while q<=qry:
            qtyp=a[i]    
            if qtyp=='SET':
                lru.set(int(a[i+1]),int(a[i+2]))
                i+=3
            elif qtyp=='GET':
                print(lru.get(int(a[i+1])),end=' ')
                i+=2
            q+=1
        print()
