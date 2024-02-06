"""
Given two integers M, N, and a 2D matrix Mat of dimensions MxN, clockwise rotate the elements in it.
"""

class Solution:
    def rotateMatrix(self, M, N, Mat):
        top = 0
        right = N - 1
        bottom = M - 1
        left = 0
        
        while top < bottom and left < right:
            prev = Mat[top + 1][left]
            
            for i in range(left, right + 1):
                prev, Mat[top][i] = Mat[top][i], prev
            top += 1
            
            for i in range(top, bottom + 1):
                prev, Mat[i][right] = Mat[i][right], prev
            right -= 1
            
            for i in range(right, left - 1, -1):
                prev, Mat[bottom][i] = Mat[bottom][i], prev
            bottom -= 1
            
            for i in range(bottom, top - 1, -1):
                prev, Mat[i][left] = Mat[i][left], prev
            left += 1
        
        return Mat

import math
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split(" "))
        A=[]
        for i in range(N):
            B=list(map(int,input().strip().split(" ")))
            A.append(B)
        ob=Solution()
        ans=ob.rotateMatrix(N,M,A)
        for i in range(N):
            for j in range(M):
                print(ans[i][j],end=" ")
            print()    