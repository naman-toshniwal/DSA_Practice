"""
Given two integers s and d. The task is to find the smallest number such that the sum of its digits is s and the number of digits in the number are d. Return a string that is the smallest possible number. If it is not possible then return -1.
"""

class Solution:
    def smallestNumber(self, s, d):
        maxv = 9 * d
        if s > maxv: 
            return -1
            
        ans = ""
        s -= 1
        
        for i in range(0, d-1):
            if s >= 9:
               ans += str(9)
               s -= 9
            else:
                ans += str(s)
                s = 0
                
        ans += str(s+1)
        ans =ans [::-1]
        return ans

import sys
import math
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1

for _ in range(t):
    s = int(data[index])
    d = int(data[index + 1])
    index += 2
    ob = Solution()
    print(ob.smallestNumber(s, d))
