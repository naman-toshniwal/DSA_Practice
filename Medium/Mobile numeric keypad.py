"""
There is a standard numeric keypad on a mobile phone. You can only press the current button or buttons that are directly up, left, right, or down from it (for ex if you press 5, then pressing 2, 4, 6 & 8 are allowed). Diagonal movements and pressing the bottom row corner buttons (* and #) are prohibited.

Given a number n, find the number of possible unique sequences of length n that you can create by pressing buttons. You can start from any digit.
"""

class Solution:
    def is_valid(self, i, j):
        if (i == 3 and j == 0) or (i == 3 and j == 2):
            return False
        
        if i < 0 or i >= 4 or j < 0 or j >= 3:
            return False
        return True
    
    def help(self, grid, i, j, n, dp):
        if not self.is_valid(i, j):
            return 0
        
        if n == 1:
            return 1
        
        if dp[i][j][n] != -1:
            return dp[i][j][n]
        result = 0
        
        if self.is_valid(i, j):
            result += self.help(grid, i, j, n - 1, dp)  
        if self.is_valid(i - 1, j):
            result += self.help(grid, i - 1, j, n - 1, dp)  
        if self.is_valid(i + 1, j):
            result += self.help(grid, i + 1, j, n - 1, dp) 
        if self.is_valid(i, j + 1):
            result += self.help(grid, i, j + 1, n - 1, dp)  
        if self.is_valid(i, j - 1):
            result += self.help(grid, i, j - 1, n - 1, dp)  

        dp[i][j][n] = result
        return result

    def getCount(self, n):
        if n <= 0:
            return 0

        grid = [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9'],
            ['*', '0', '#']
        ]

        ans = 0
        dp = [[[-1 for _ in range(n + 1)] for _ in range(3)] for _ in range(4)]
        
        for i in range(4):
            for j in range(3):
                if self.is_valid(i, j):
                    ans += self.help(grid, i, j, n, dp)
        
        return ans

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        ob = Solution()
        ans = ob.getCount(n)
        print(ans)
