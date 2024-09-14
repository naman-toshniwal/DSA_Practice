"""
Given an array arr containing the lengths of the different ropes, we need to connect these ropes to form one rope. The cost to connect two ropes is equal to sum of their lengths. The task is to connect the ropes with minimum cost.  
"""

import heapq

class Solution:
   def minCost(self, arr) -> int:
        heapq.heapify(arr)
        cost = 0
        
        while len(arr) > 1:
            rope1 = heapq.heappop(arr)
            rope2 = heapq.heappop(arr)
            res = rope1 + rope2
            cost += res
            heapq.heappush(arr, res)
            
        return cost

import atexit
import io
import sys
import heapq
from collections import defaultdict

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        a = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.minCost(a))
