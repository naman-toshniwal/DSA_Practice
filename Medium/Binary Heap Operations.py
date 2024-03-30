"""
A binary heap is a Binary Tree with the following properties:
1) Its a complete tree (All levels are completely filled except possibly the last level and the last level has all keys as left as possible). This property of Binary Heap makes them suitable to be stored in an array.

2) A Binary Heap is either Min Heap or Max Heap. In a Min Binary Heap, the key at the root must be minimum among all keys present in Binary Heap. The same property must be recursively true for all nodes in Binary Tree. Max Binary Heap is similar to MinHeap.

You are given an empty Binary Min Heap and some queries and your task is to implement the three methods insertKey,  deleteKey,  and extractMin on the Binary Min Heap and call them as per the query given below:
1) 1  x  (a query of this type means to insert an element in the min-heap with value x )
2) 2  x  (a query of this type means to remove an element at position x from the min-heap)
3) 3  (a query like this removes the min element from the min-heap and prints it ).
"""

heap = [0 for i in range(101)]

def insertKey(x):
    global curr_size
    curr_size += 1
    i = curr_size - 1
    heap[i] = x
    
    while i > 0 and heap[(i - 1) // 2] > heap[i]:
        heap[i], heap[(i - 1) // 2] = heap[(i - 1) // 2], heap[i]
        i = (i - 1) // 2

def deleteKey(i):
    global curr_size
    
    if i >= curr_size:
        return
    else:
        heap[i] = float('-inf')
        
        while i!=0 and heap[(i-1)//2]>heap[i]:
            heap[i], heap[(i - 1) // 2] = heap[(i - 1) // 2], heap[i]
            i=(i-1)//2
        extractMin()


def minHeapify(i):
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    smallest = i
    
    if left_child < curr_size and heap[left_child] < heap[smallest]:
        smallest = left_child
    
    if right_child < curr_size and heap[right_child] < heap[smallest]:
        smallest = right_child
    
    if smallest != i:
        heap[i], heap[smallest] = heap[smallest], heap[i]
        minHeapify(smallest)

def extractMin():
    global curr_size
    
    if curr_size > 0:
        min_val = heap[0]
        heap[0] = heap[curr_size - 1]
        minHeapify(0)
        curr_size -= 1
        return min_val
    else:
        return -1

import atexit
import io
import sys
_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER
@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

heap = []  # 
curr_size = 0  

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int, input().strip().split()))
        curr_size = 0
        heap = [0 for i in range(n)]
        i = 0
        
        while i < len(a):
            if a[i] == 1:
                insertKey(a[i + 1])
                i += 1
            elif a[i] == 2:
                deleteKey(a[i + 1])
                i += 1
            else:
                print(extractMin (), end=" ")
            i += 1
        print()
