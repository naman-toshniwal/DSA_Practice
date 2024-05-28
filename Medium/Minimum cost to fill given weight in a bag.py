"""
Given an array cost[] of positive integers of size n and an integer w, where cost[i] represents the cost of an i kg packet of oranges, the task is to find the minimum cost to buy exactly w kg of oranges. The cost array has a 1-based indexing. If buying exactly w kg of oranges is impossible, then return -1.
Note:
1. cost[i] = -1 means that i kg packet of orange is unavailable.
2. It may be assumed that there is an infinite supply of all available packet types.
"""

from typing import List

class Solution:
    def mincost(self, cost, ind, w, dp):
        if(w==0):
            return 0
        
        if(ind<0):
            return 2**32
        
        if(cost[ind]==-1):
            return 2**32
        
        if(dp[ind][w]!=-1):
            return dp[ind][w]
        notpick = self.mincost(cost, ind-1, w, dp)
        pick = 2**32
        
        if(ind+1<=w):
            pick = self.mincost(cost, ind, w-ind-1, dp) + cost[ind]
        dp[ind][w] = min(pick,notpick)
        return dp[ind][w]
    
    def minimumCost(self, n : int, w : int, cost : List[int]) -> int:
        dp = [[-1 for i in range(w+1)] for i in range(n)]
        self.mincost(cost, n-1, w, dp)
        return dp[-1][-1]

class IntArray:
    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        w = int(input())
        cost = IntArray().Input(n)
        obj = Solution()
        res = obj.minimumCost(n, w, cost)
        print(res)
