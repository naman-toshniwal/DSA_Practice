"""
Given N activities with their start and finish day given in array start[ ] and end[ ]. Select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a given day.
Note : Duration of the activity includes both starting and ending day.
"""

class Solution:
    def activitySelection(self,n,start,end):
        c=0
        zipped_arr = list(zip(start, end))
        zipped_arr.sort(key=lambda x: x[1])
        temp=float('-inf')
        
        for i, j in zipped_arr:
            if i>temp:
                c+=1
                temp=j
        return c

import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.activitySelection(n,start,end))
