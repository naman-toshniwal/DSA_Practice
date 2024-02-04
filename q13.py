"""
Given a string str and another string patt. Find the minimum index of the character in str that is also present in patt.
"""

class Solution:
    def minIndexChar(self,Str, pat): 
        for i in range(len(Str)):
            if Str[i] in pat:
                return i        
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

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        obj = Solution()
        ans = obj.minIndexChar(s,p)
        print(ans)