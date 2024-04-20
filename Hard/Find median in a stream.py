"""
Given an input stream of N integers. The task is to insert these numbers into a new stream and find the median of the stream formed by each insertion of X to the new stream.
"""

import atexit
import io
import sys
import heapq
from collections import  defaultdict
import math
from sortedcontainers import *

class Solution:
    def __init__(self):
        self.arr=SortedList([])
    
    def getMedian(self):
        n=len(self.arr)
        if n%2==0:
            return (self.arr[n//2]+self.arr[n//2-1])//2
        else:
            return self.arr[n//2]

    def insertHeaps(self,x):
        self.arr.add(x)

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        ob=Solution()
        for i in range(n):
            x=int(input())
            ob.insertHeaps(x)
            print(math.floor(ob.getMedian()))
