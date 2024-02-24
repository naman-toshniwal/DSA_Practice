"""
A frog jumps either 1, 2, or 3 steps to go to the top. In how many ways can it reach the top of Nth step. As the answer will be large find the answer modulo 1000000007.
"""

class Solution:
    def countWays(self,n):
        mod = 1000000007
        dp = [0 for i in range(n+69)]
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4
        
        for i in range(4, n+3):
            dp[i] += dp[i-1] + dp[i-2] + dp[i-3]
        
        return dp[n] % mod

import atexit
import io
import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob=Solution()
        print(ob.countWays(m))
