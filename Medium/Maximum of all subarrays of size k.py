"""
Given an array arr[] of size N and an integer K. Find the maximum for each and every contiguous subarray of size K.
"""

class Solution:
    def max_of_subarrays(self,arr,n,k):
        q = deque()
        ans = []
        
        for i in range(k-1):
            while q and arr[i] >= arr[q[-1]]:
                q.pop()
            q.append(i)
        
        for i in range(k-1, n):
            while q and arr[i] >= arr[q[-1]]:
                q.pop()
            q.append(i)
            
            if q[0] <= i - k:
                q.popleft()
            ans.append(arr[q[0]])
        return ans

import atexit
import io
import sys
from collections import deque
_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER
@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,k = map(int,input().strip().split())
        arr = list(map(int,input().strip().split()))
        ob=Solution()
        res = ob.max_of_subarrays(arr,n,k)
        for i in range (len (res)):
            print (res[i], end = " ")
        print()
