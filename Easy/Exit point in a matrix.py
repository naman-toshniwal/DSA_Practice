"""
Given a matrix of size n x m with 0’s and 1’s, you enter the matrix at cell (0,0) in left to right direction. Whenever you encounter a 0 you retain it in the same direction, else if you encounter a 1 you have to change the direction to the right of the current direction and change that 1 value to 0, you have to find out from which index you will leave the matrix at the end.
"""

class Solution:
    def FindExitPoint(self, n, m, mat):
        i,j,d=0,0,0
        
        while (0<=i<n and 0<=j<m):
            if mat[i][j]==1:
                mat[i][j]=0
                d=(d+1)%4
            
            if d==0: 
                j+=1
            elif d==1: 
                i+=1
            elif d==2: 
                j-=1
            else: 
                i-=1
        
        if d==0: 
            return (i,j-1)
        elif d==1: 
            return (i-1,j)
        elif d==2: 
            return (i,j+1)
        return (i+1,j)

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, m = input().split()
        n = int(n)
        m = int(m)
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, input().split())))
        ob = Solution()
        ans = ob.FindExitPoint(n, m, matrix)
        for _ in ans:
            print(_, end=" ")
        print()
