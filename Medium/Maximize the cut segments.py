"""
Given an integer N denoting the Length of a line segment. You need to cut the line segment in such a way that the cut length of a line segment each time is either x , y or z. Here x, y, and z are integers.
After performing all the cut operations, your total number of cut segments must be maximum.

Note: if no segment can be cut then return 0.
"""

class Solution:
    def maximizeTheCuts(self, N, x, y, z):
        memo = [-1] * (N + 1)
        memo[0] = 0 

        for i in range(1, N + 1):
            if i - x >= 0:
                memo[i] = max(memo[i], memo[i - x])
            
            if i - y >= 0:
                memo[i] = max(memo[i], memo[i - y])
            
            if i - z >= 0:
                memo[i] = max(memo[i], memo[i - z])

            if memo[i] != -1:
                memo[i] += 1

        return memo[N] if memo[N] != -1 else 0

if __name__ == '__main__':
    t=int(input())
    for tcs in range(t):
        n=int(input())
        x,y,z=[int(x) for x in input().split()]
        
        print(Solution().maximizeTheCuts(n,x,y,z))
