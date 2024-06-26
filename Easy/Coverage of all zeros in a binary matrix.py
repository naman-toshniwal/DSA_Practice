"""
Given a binary matrix contains 0s and 1s only, we need to find the sum of coverage of all zeros of the matrix where coverage for a particular 0 is defined as a total number of ones around a zero in left, right, up and bottom directions.

Note: The ones considered to be anywhere till the corner point in a direction. 
"""

class Solution:
    def findCoverage(self, matrix):
        row, col = len(matrix), len(matrix[0])
        count = 0
       
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    if -1 < i-1 < row and matrix[i-1][j] == 1:
                        count += 1
                    if -1 < j-1 < col and matrix[i][j-1] == 1:
                        count += 1
                    if -1 < j+1 < col and matrix[i][j+1] == 1:
                        count += 1
                    if -1 < i+1 < row and matrix[i+1][j] == 1:
                        count += 1
                        
        return count

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
        ans = ob.findCoverage(matrix)
        print(ans)
