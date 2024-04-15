"""
Given an incomplete Sudoku configuration in terms of a 9 x 9  2-D square matrix (grid[][]), the task is to find a solved Sudoku. For simplicity, you may assume that there will be only one unique solution.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Zeros in the grid indicates blanks, which are to be filled with some number between 1-9. You can not replace the element in the cell which is not blank.
"""

class Solution:
    def is_safe(self, ar, row, col, num):
        for i in range(9):
            if ar[row][i] == num or ar[i][col] == num:
                return False
        
        sub_row = (row // 3) * 3
        sub_col = (col // 3) * 3
        
        for i in range(sub_row, sub_row+3):
            for j in range(sub_col, sub_col+3):
                if ar[i][j] == num:
                    return False
        
        return True
    
    def get_sudoku_sol(self, ar, curr_idx=0):
        if (curr_idx == 81):
            return True
        
        row = curr_idx // 9
        col = curr_idx % 9
        
        if ar[row][col] == 0:
            for num in range(1, 10):
                if self.is_safe(ar, row, col, num):
                    ar[row][col] = num
                    
                    if self.get_sudoku_sol(ar, curr_idx+1):
                        return True
                    ar[row][col] = 0
           
            return False
        return self.get_sudoku_sol(ar, curr_idx+1)
    
    def SolveSudoku(self,grid):
        if self.get_sudoku_sol(grid):
            return True
        return False
      
    def printGrid(self,ar):
        for i in range(9):
            print(*ar[i], sep=" ", end=" ")

if __name__=="__main__":
    t = int(input())
    while(t>0):
        grid = [[0 for i in range(9)] for j in range(9)]
        row = [int(x) for x in input().strip().split()]
        k = 0
        for i in range(9):
            for j in range(9):
                grid[i][j] = row[k]
                k+=1
        ob = Solution()
            
        if(ob.SolveSudoku(grid)==True):
            ob.printGrid(grid)
            print()
        else:
            print("No solution exists")
        t = t-1
