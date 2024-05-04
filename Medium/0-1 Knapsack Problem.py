"""
You are given weights and values of N items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. Note that we have only one quantity of each item.
In other words, given two integer arrays val[0..N-1] and wt[0..N-1] which represent values and weights associated with N items respectively. Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. You cannot break an item, either pick the complete item or dont pick it (0-1 property).
"""

class Solution:
    def knapSack(self, W, wt, val, n):
        memo = {}
    
        def solver(i, W):
            if (i, W) in memo:
                return memo[(i, W)]
    
            if i == n or W == 0:
                return 0
    
            elif wt[i] > W:
                return solver(i + 1, W)
    
            else:
                include = val[i] + solver(i + 1, W - wt[i])
                exclude = solver(i + 1, W)
                memo[(i, W)] = max(include, exclude)
                return memo[(i, W)]
    
        return solver(0, W)

import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
