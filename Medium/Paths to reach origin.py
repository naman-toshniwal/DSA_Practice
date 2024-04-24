"""
You are standing on a point (x, y) and you want to go to origin (0, 0) by taking steps either left or up i.e. from each point you are allowed to move either in (x-1, y) or (x, y-1). Find the number of paths from point to origin.
"""

class Solution:
    def ways(self, x, y):
        mod = 1000000007
        dp = [0] * (min(x, y) + 1)
        dp[0] = 1

        for i in range(1, min(x, y) + 1):
            dp[i] = (dp[i - 1] * (x + y - i + 1) * pow(i, mod - 2, mod)) % mod
        return dp[min(x, y)]

t=int(input())
for _ in range(0,t):
    x,y=list(map(int,input().split()))
    ob = Solution()
    print(ob.ways(x,y))
