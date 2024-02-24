"""
Implement a Stack using two queues q1 and q2.
"""

'''
    :param x: value to be inserted
    :return: None

    queue_1 = Queue() # first queue
    queue_2 = Queue() # second queue
'''

from queue import Queue   

def push(x):
    global queue_1
    global queue_2
    queue_1.put(x)

def pop():
    global queue_1
    global queue_2
    s = queue_1.qsize()
    
    if s == 0:
        return -1
    
    while queue_1.qsize() != 1:
        queue_2.put(queue_1.get())
        
    while queue_2.empty() == False:
        queue_1.put(queue_2.get())
    return queue_1.get()
    
from queue import Queue

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        queue_1 = Queue() 
        queue_2 = Queue() 
        n = int(input())
        a = list(map(int,input().strip().split()))
        i = 0
        while i<len(a):
            if a[i] == 1:
                push(a[i+1])
                i+=1
            else:
                print(pop(),end=" ")
            i+=1
            
        print()
