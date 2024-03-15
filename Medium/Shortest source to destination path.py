"""
Given a 2D binary matrix A(0-based index) of dimensions NxM. Find the minimum number of steps required to reach from (0,0) to (X, Y).
Note: You can only move left, right, up and down, and only through cells that contain 1.
"""

class Solution:
    def shortestDistance(self,N,M,A,X,Y):
        if A[0][0] == 0:
            return -1
        
        vis = set()
        q = [(0, 0)]
        result = -1
        
        while q:
            l = len(q)
            result += 1
            
            for _ in range(l):
                r, c = q.pop(0)
                
                if r == X and c == Y:
                    return result
                
                for x, y in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                    if x >= 0 and y >= 0 and x < N and y < M and (x, y) not in vis and A[x][y] == 1:
                        q.append((x, y))
                        vis.add((x, y))
        
        return -1

import math 
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split())
        a=[]
        for i in range(N):
            s=list(map(int,input().strip().split()))
            a.append(s)
        x,y=map(int,input().strip().split())    
        ob=Solution()
        print(ob.shortestDistance(N,M,a,x,y))
