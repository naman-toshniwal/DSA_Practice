"""
Given a grid of dimension nxm where each cell in the grid can have values 0, 1 or 2 which has the following meaning:
0 : Empty cell
1 : Cells have fresh oranges
2 : Cells have rotten oranges

We have to determine what is the earliest time after which all the oranges are rotten. A rotten orange at index [i,j] can rot other fresh orange at indexes [i-1,j], [i+1,j], [i,j-1], [i,j+1] (up, down, left and right) in unit time. 
"""

from collections import deque

class Solution:
    def orangesRotting(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        fresh = time = 0
        q = deque()
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))
            
        directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]
        
        while q and fresh > 0:
            for i in range(len(q)):
                row, col = q.popleft()
                
                for nr, nc in directions:
                    r = nr + row
                    c = nc + col
                    
                    if r in range(rows) and c in range(cols) and grid[r][c] == 1:
                        grid[r][c] = 2
                        fresh -= 1
                        q.append((r, c))
                        
            time += 1
        return time if fresh == 0 else -1
    
T=int(input())
for i in range(T):
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        a = list(map(int, input().split()))
        grid.append(a)
    obj = Solution()
    ans = obj.orangesRotting(grid)
    print(ans)
