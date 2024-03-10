"""
Given a matrix of size n x m, where every row and column is sorted in increasing order, and a number x. Find whether element x is present in the matrix or not.
"""

class Solution:
    def search(self,matrix, n, m, x): 
        row, col = 0, m - 1
        
        while row < n and col >= 0:
            if matrix[row][col] == x:
                return 1
            elif matrix [row][col] < x:
                row += 1
            else:
                col -= 1        
        return 0

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        size = input().strip().split()
        r = int(size[0])
        c = int(size[1])
        line = input().strip().split()
        matrix = [ [0 for _ in range(c)] for _ in range(r) ]
        for i in range(r):
            for j in range(c):
                matrix[i][j] = int( line[i*c+j] )
        target = int(input())
        obj = Solution()
        if (obj.search(matrix,r,c,target)): 
            print(1) 
        else: 
            print(0) 
