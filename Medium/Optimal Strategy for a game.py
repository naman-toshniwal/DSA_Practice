"""
You are given an array arr of size n. The elements of the array represent n coin of values v1, v2, ....vn. You play against an opponent in an alternating way. In each turn, a player selects either the first or last coin from the row, removes it from the row permanently, and receives the value of the coin.
You need to determine the maximum possible amount of money you can win if you go first.
Note: Both the players are playing optimally.
"""

class Solution:
    def optimalStrategyOfGame(self, n, arr):
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = arr[i]

        for gap in range(1, n):
            for i in range(n - gap):
                j = i + gap

                if gap == 1:
                    dp[i][j] = max(arr[i], arr[j])
                else:
                    pick_start = arr[i] + min(dp[i + 2][j], dp[i + 1][j - 1])
                    pick_end = arr[j] + min(dp[i + 1][j - 1], dp[i][j - 2])
                    dp[i][j] = max(pick_start, pick_end)

        return dp[0][n - 1]

import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int,input().strip().split()))
        ob = Solution()
        print(ob.optimalStrategyOfGame(n,arr))
