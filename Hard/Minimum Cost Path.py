"""
Given a square grid of size N, each cell of which contains integer cost which represents a cost to traverse through that cell, we need to find a path from top left cell to bottom right cell by which the total cost incurred is minimum.
From the cell (i,j) we can go (i,j-1), (i, j+1), (i-1, j), (i+1, j). 

Note: It is assumed that negative cost cycles do not exist in the input matrix.
"""

from functools import cmp_to_key
import heapq

class cell:
    def __init__(self,x,y,dist):
        self.x=x
        self.y=y
        self.dist=dist

class Solution:
    def minimumCostPath(self, grid):
        n=len(grid)
        dis=[[float('inf') for i in range(n)]for j in range(n)]
        dis[0][0]=grid[0][0]
        st=[]
        dxi = [-1, 0, 1, 0]
        dyi = [0, 1, 0, -1]
        heapq.heappush(st,(dis[0][0],0,0))

        while len(st)!=0:
            dist, x, y = heapq.heappop(st)

            if dis[x][y] < dist:
                continue

            for i in range(4):
                dx=x+dxi[i]
                dy=y+dyi[i]

                if(dx>=0 and dx<n and dy>=0 and dy<n and dis[dx][dy]>dis[x][y]+grid[dx][dy]): 
                    dis[dx][dy]=dis[x][y]+grid[dx][dy]
                    heapq.heappush(st,(dis[dx][dy],dx,dy))
            
        return dis[n-1][n-1]

T=int(input())
for i in range(T):
    n = int(input())
    grid = []
    for _ in range(n):
        a = list(map(int, input().split()))
        grid.append(a)
    obj = Solution()
    ans = obj.minimumCostPath(grid)
    print(ans)
