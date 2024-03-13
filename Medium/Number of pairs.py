"""
Given two arrays X and Y of positive integers, find the number of pairs such that xy > yx (raised to power of) where x is an element from X and y is an element from Y.
"""

from bisect import bisect as bi

class Solution: 
    def countPairs(self,a,b,M,N):
        a.sort()
        b.sort()
        count = 0
        for x in a:
            if x == 1:
                continue
            elif x == 2:
                count+=bi(b,1)+N-bi(b,4)
            elif x==3:
                count+=bi(b,2)+N-bi(b,3)
            else:
                count+=bi(b,1)+N-bi(b,x)
        return count


import atexit
import io
import sys
import bisect

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER
@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        M,N=map(int,input().strip().split())
        a=list(map(int,input().strip().split()))
        b=list(map(int,input().strip().split()))
        ob=Solution();
        print(ob.countPairs(a,b,M,N))
