"""
The n-queens puzzle is the problem of placing n queens on a (n×n) chessboard such that no two queens can attack each other.
Given an integer n, find all distinct solutions to the n-queens puzzle. Each solution contains distinct board configurations of the n-queens’ placement, where the solutions are a permutation of [1,2,3..n] in increasing order, here the number in the ith place denotes that the ith-column queen is placed in the row with that number. For eg below figure represents a chessboard [3 1 4 2].
"""

class Solution:
    def solve(self,row,col,n,board):
        for i in range(col):
            if board[row][i]==1:
                return False
        
        for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
            if board[i][j]==1:
                return False
        
        for i,j in zip(range(row,n),range(col,-1,-1)):
            if board[i][j]==1:
                return False
        
        return True
    
    def add_solution(self,board,solution,n):
        temp=[]
        for i in range(n):
            for j in range(n):
                if board[j][i]:
                    temp.append(j+1)
                
        solution.append(temp)
    
    def solve_queen(self,col,n,board,solution):
        if col==n:
            self.add_solution(board,solution,n)
            return True
            
        for i in range(n):
            if self.solve(i,col,n,board):
                board[i][col]=1
                self.solve_queen(col+1,n,board,solution)
                board[i][col]=0
                
    
    def nQueen(self, n):
        board = [[0] * n for _ in range(n)]
        solution=[]
        self.solve_queen(0,n,board,solution)
        return solution

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        ans = ob.nQueen(n)

        if(len(ans) == 0):
            print("-1")
        else:
            for i in range(len(ans)):
                print("[",end="")
                for j in range(len(ans[i])):
                    print(ans[i][j],end = " ")
                print("]",end = " ")
            print()
