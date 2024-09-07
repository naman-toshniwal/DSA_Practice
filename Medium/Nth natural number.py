"""
Given a positive integer n. You have to find nth natural number after removing all the numbers containing the digit 9.
"""

def solve(n):
    if n<9:
        return n
    return 10*solve(n//9)+n%9

class Solution:
    def findNth(self,n):
        return solve(n)

t = int(input())
for i in range(0, t):
    n = int(input())
    obj = Solution()
    s = obj.findNth(n)
    print(s)
