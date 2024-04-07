"""
Given a 5x6 snakes and ladders board, find the minimum number of dice throws required to reach the destination or last cell (30th cell) from the source (1st cell).

You are given an integer N denoting the total number of snakes and ladders and an array arr[] of 2*N size where 2*i and (2*i + 1)th values denote the starting and ending point respectively of ith snake or ladder. The board looks like the following.
Note: Assume that you have complete control over the 6 sided dice. No ladder starts from 1st cell.
"""

import collections

class Solution:
    def minThrow(self, N, arr):
        q = collections.deque()
        visited = [False for i in range(31)]
        q.appendleft([1,0])
    
        while (len(q) != 0):
            id, hop = q.popleft()
            
            for i in range(1,7):
                next = id + i
                
                if next in arr and arr.index(next)%2 == 0:
                    next = arr[arr.index(next)+1]
                
                if next == 30:
                    return hop + 1
                
                if visited[next-1] != True:
                    visited[next-1] = True
                    q.append([next, hop+1])

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(2*N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.minThrow(N, arr))
