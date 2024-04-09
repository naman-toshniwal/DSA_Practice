"""
Given a m*n grid with each cell consisting of positive, negative, or zero point. We can move across a cell only if we have positive points. Whenever we pass through a cell, points in that cell are added to our overall points, the task is to find minimum initial points to reach cell (m-1, n-1) from (0, 0) by following these certain set of rules :
1. From a cell (i, j) we can move to (i + 1, j) or (i, j + 1).
2. We cannot move from (i, j) if your overall points at (i, j) are <= 0.
3. We have to reach at (n-1, m-1) with minimum positive points i.e., > 0.
"""

class Solution:
    def minPoints(self, m, n, points):
        dp = [[0] * n for _ in range(m)]
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    dp[i][j] = max(1, 1 - points[i][j])
                elif i == m - 1:
                    dp[i][j] = max(1, dp[i][j + 1] - points[i][j])
                elif j == n - 1:
                    dp[i][j] = max(1, dp[i + 1][j] - points[i][j])
                else:
                    dp[i][j] = max(1, min(dp[i + 1][j], dp[i][j + 1]) - points[i][j])
        
        return dp[0][0]

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        m,n = input().split()
        m,n = int(m),int(n)
        points = []
        for _ in range(m):
            temp = [int(x) for x in input().split()]
            points.append(temp)
        ob = Solution()
        ans = ob.minPoints(m,n,points)
        print(ans)
