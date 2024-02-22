"""
There is one meeting room in a firm. There are N meetings in the form of (start[i], end[i]) where start[i] is start time of meeting i and end[i] is finish time of meeting i.
What is the maximum number of meetings that can be accommodated in the meeting room when only one meeting can be held in the meeting room at a particular time?

Note: Start time of one chosen meeting can't be equal to the end time of the other chosen meeting.
"""

class Solution:
    def maximumMeetings(self,n,start,end):
        l = list(zip(start, end))
        l.sort(key = lambda x:x[1])
        count = 1
        endli = l[0][1]
        
        for i in range(1, n):
            if endli < l[i][0]:
                endli = l[i][1]
                count += 1
        return count

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
        print(ob.maximumMeetings(n,start,end))
