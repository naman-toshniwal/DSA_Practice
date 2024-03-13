"""
Given an array of positive integers. Find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers, the consecutive numbers can be in any order.
"""

class Solution:
    def findLongestConseqSubseq(self,arr, N):
        arr = list(set(arr))
        arr.sort()
        longest_length = 0
        current_length = 1
        
        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1] + 1:
                current_length += 1
            else:
                longest_length = max(longest_length, current_length)
                current_length = 1
        
        longest_length = max(longest_length, current_length)
        return longest_length


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

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n=int(input())
        a = list(map(int, input().strip().split()))
        print(Solution().findLongestConseqSubseq(a,n))
