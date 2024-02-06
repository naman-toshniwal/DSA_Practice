"""
Given a binary matrix your task is to find all unique rows of the given matrix in the order of their appearance in the matrix.
"""

from typing import List
class Solution:
    def uniqueRow(self, row : int, col : int, M : List[List[int]]) -> List[List[int]]:
        result = []
        
        for i in range(row):
            row_tuple = tuple(M[i])
            if row_tuple not in result:
                result.append(row_tuple)
        
        return result

def main():
    testcase = int(input())
    while(testcase):
        s = input().split()
        row = int(s[0])
        col = int(s[1])
        matrix = [[None for _ in range(col)]for _ in range(row)]
        s = input().split()
        for i in range(row):
            for j in range(col):
                matrix[i][j] = int(s[i*col+j])
        
        ob = Solution()
        a = ob.uniqueRow(row, col, matrix)
        
        for row in a:
            for value in row:
                print(value,end = " ")
            print("$",end = "")
        print()
        testcase -= 1

if __name__ == "__main__":
    main()