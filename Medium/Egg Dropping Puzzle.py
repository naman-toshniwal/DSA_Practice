"""
You are given N identical eggs and you have access to a K-floored building from 1 to K.

There exists a floor f where 0 <= f <= K such that any egg dropped from a floor higher than f will break, and any egg dropped from or below floor f will not break.
There are few rules given below. 

An egg that survives a fall can be used again.
A broken egg must be discarded.
The effect of a fall is the same for all eggs.
If the egg doesn't break at a certain floor, it will not break at any floor below.
If the eggs breaks at a certain floor, it will break at any floor above.
Return the minimum number of moves that you need to determine with certainty what the value of f is.
"""

class Solution:
    def eggDrop(self,n, k):
        dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
        
        for i in range(1, k + 1):
            dp[1][i] = i
        
        for i in range(1, n + 1):
            dp[i][1] = 1
        
        for i in range(2, n + 1):
            for j in range(2, k + 1):
                dp[i][j] = float("inf")
        
                for x in range(1, j + 1):
                    res = 1 + max(dp[i - 1][x - 1], dp[i][j - x])
                    if res < dp[i][j]:
                        dp[i][j] = res
     
        return dp[n][k]

import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n,k = map(int,input().strip().split())
        ob=Solution()
        print(ob.eggDrop(n,k))
