"""
Given two integers n, m and a 2D matrix mat of dimensions nxm, the task is to find the maximum sum of an hourglass.
An hourglass is defined as a part of the matrix with the following form:
A B C
  D
E F G

Return -1 if any hourglass is not found.
"""

class Solution:
    def findMaxSum(self, n, m, mat):
        max_sum = -1  
        
        for i in range(n - 2):
            for j in range(m - 2):
                if (i + 2 < n) and (j + 2 < m):
                    hourglass_sum = (
                        mat[i][j] + mat[i][j + 1] + mat[i][j + 2] +
                        mat[i + 1][j + 1] +
                        mat[i + 2][j] + mat[i + 2][j + 1] + mat[i + 2][j + 2]
                    )
                    max_sum = max(max_sum, hourglass_sum)

        return max_sum

import math
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split(" "))
        Mat=[]
        for i in range(N):
            B=list(map(int,input().strip().split(" ")))
            Mat.append(B)
        ob=Solution()
        ans=ob.findMaxSum(N,M,Mat)
        print(ans) 
