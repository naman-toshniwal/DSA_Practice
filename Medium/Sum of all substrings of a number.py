"""
Given an integer s represented as a string, the task is to get the sum of all possible sub-strings of this string.
As the answer will be large, return answer modulo 109+7. 
Note: The number may have leading zeros.
"""

class Solution:
    def sumSubstrings(self,s):
        mod = 10**9 + 7
        n = len(s)
        total_sum = 0
        position_sum = 0
        
        for i in range(n):
            position_sum = (position_sum * 10 + int(s[i]) * (i + 1)) % mod
            total_sum = (total_sum + position_sum) % mod
        return str(total_sum)

import atexit
import io
import sys
import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        s = str(input())
        ob=Solution()
        print(ob.sumSubstrings(s))
