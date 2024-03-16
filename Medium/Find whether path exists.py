"""
Given a grid of size n*n filled with 0, 1, 2, 3. Check whether there is a path possible from the source to destination. You can traverse up, down, right and left.
The description of cells is as follows:

A value of cell 1 means Source.
A value of cell 2 means Destination.
A value of cell 3 means Blank cell.
A value of cell 0 means Wall.
Note: There are only a single source and a single destination.
"""

from collections import deque

class Solution:
    def is_Possible(self, grid):
        n = len(grid)
        source = []
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    source = [i, j]
            
        q = deque()
        q.append((source[0], source[1]))
        
        while q:
            row, col = q.popleft()
            for i, j in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                newR, newC = row+i, col+j
                
                if newR>=0 and newR<n and newC>=0 and newC<n and grid[newR][newC] not in (0, 1):
                    if grid[newR][newC] == 2:
                        return True
                    q.append((newR, newC))
                    grid[newR][newC] = 0
        
        return False

T=int(input())
for i in range(T):
    n = int(input())
    grid = []
    for _ in range(n):
        a = list(map(int, input().split()))
        grid.append(a)
    obj = Solution()
    ans = obj.is_Possible(grid)
    if(ans):
        print("1")
    else:
        print("0")
