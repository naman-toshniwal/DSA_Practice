"""
Given an integer array coins[ ] of size N representing different denominations of currency and an integer sum, find the number of ways you can make sum by using different combinations from coins[ ].  
Note: Assume that you have an infinite supply of each type of coin. And you can use any coin as many times as you want.
"""

class Solution:
    def count(self, coins, N, Sum):
        ch = [0] * (Sum + 1)
        ch[0] = 1
        
        for coin in coins:
            for i in range(coin, Sum+1):
                ch[i] += ch[i - coin]
                
        return ch[Sum]

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        sum,N = list(map(int, input().strip().split()))
        coins = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.count(coins,N,sum))
