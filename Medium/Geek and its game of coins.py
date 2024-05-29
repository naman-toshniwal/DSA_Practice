"""
Given three numbers n, x, and y, Geek and his friend are playing a coin game. In the beginning, there are n coins. In each move, a player can pick x, y, or 1 coin. Geek always starts the game. The player who picks the last coin wins the game. The task is to determine whether Geek will win the game or not if both players play optimally.
"""

class Solution:
    def findWinner(self, n : int, x : int, y : int) -> int:
        dp = [True] * (n + 1)
        
        for i in range(2, n + 1):
            dp[i] = (
                    i - x == 0 or
                    i - y == 0 or
                    (i - 1 > 0 and not dp[i - 1]) or
                    (i - x > 0 and not dp[i - x]) or
                    (i - y > 0 and not dp[i - y])
                )
        return int(dp[n])

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        x = int(input())
        y = int(input())
        obj = Solution()
        res = obj.findWinner(n, x, y)
        print(res)
