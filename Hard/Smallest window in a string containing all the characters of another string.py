"""
Given two strings S and P. Find the smallest window in the string S consisting of all the characters(including duplicates) of the string P.  Return "-1" in case there is no such window present. In case there are multiple such windows of same length, return the one with the least starting index.
Note : All characters are in Lowercase alphabets. 
"""

class Solution:
    def smallestWindow(self, s: str, p: str) -> str:
        freq_p = {}
        
        for char in p:
            freq_p[char] = freq_p.get(char, 0) + 1
        
        start = 0
        end = 0
        min_window = float('inf')
        min_start = 0
        remaining_chars = len(p)
        
        while end < len(s):
            if s[end] in freq_p:
                freq_p[s[end]] -= 1
                if freq_p[s[end]] >= 0:
                    remaining_chars -= 1
            
            end += 1
            
            while remaining_chars == 0:
                if end - start < min_window:
                    min_window = end - start
                    min_start = start
                
                if s[start] in freq_p:
                    freq_p[s[start]] += 1
                    if freq_p[s[start]] > 0:
                        remaining_chars += 1
                
                start += 1
        
        if min_window == float('inf'):
            return -1
        return s[min_start:min_start + min_window]

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
        ob = Solution()
        print(ob.smallestWindow(s,p))
