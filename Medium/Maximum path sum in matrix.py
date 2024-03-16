"""
Given a NxN matrix of positive integers. There are only three possible moves from a cell Matrix[r][c].

Matrix [r+1] [c]
Matrix [r+1] [c-1]
Matrix [r+1] [c+1]
Starting from any column in row 0 return the largest sum of any of the paths up to row N-1.

NOTE: We can start from any column in zeroth row and can end at any column in (N-1)th row.
"""

class Solution:
    def maximumPath(self, N, Matrix):
        dp = [[-1 for j in range(N)] for i in range(N)]
        dp[N-1]  = Matrix[N-1][:]
        
        for i in range(N-2, -1, -1):
            for j in range(N):
                left = dp[i+1][j-1] if j>0 else float('-inf')
                middle = dp[i+1][j]
                right = dp[i+1][j+1] if j<(N-1) else float('-inf')
                dp[i][j] = max(left, middle, right) + Matrix[i][j]
                
        return max(dp[0])

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        Matrix = [[0]*N for i in range(N)]
        for itr in range(N*N):
            Matrix[(itr//N)][itr%N] = int(arr[itr])
        
        ob = Solution()
        print(ob.maximumPath(N, Matrix))
