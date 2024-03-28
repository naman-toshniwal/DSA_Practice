"""
There are n cities labeled from 0 to n-1 with m edges connecting them. Given the array edges where edges[i] = [fromi , toi ,weighti]  represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold. You need to find out a city with the smallest number of cities that are reachable through some path and whose distance is at most Threshold Distance. If there are multiple such cities, our answer will be the city with the greatest label.

Note: The distance of a path connecting cities i and j is equal to the sum of the edge's weights along that path.
"""

from typing import List
class Solution:
    def findCity(self, n : int, m : int, edges : List[List[int]], d : int) -> int:
        from collections import defaultdict
        from heapq import heappush, heappop
        g = defaultdict(list)
        
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w))
        
        def dijkstr(n):
            costs = {n: 0}
            q = [(0, n)]
            
            while q:
                cost0, n0 = heappop(q)
            
                for nbr, c in g[n0]:
                    cost = cost0+c
            
                    if cost > d:
                        continue
            
                    if nbr not in costs or costs[nbr] > cost:
                        costs[nbr] = cost
                        heappush(q, (cost, nbr))
            
            return len(costs)
            
        ans = 0
        cnt = n
        for k in range(n):
            c = dijkstr(k)
            
            if c <= cnt:
                cnt = c
                ans = k
        return ans

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        n, m = map(int, input().strip().split())
        edges = []

        for i in range(m):
            u, v, wt = map(int, input().strip().split())
            edges.append([u, v, wt])
        distanceThreshold = int(input())
        obj = Solution()
        ans = obj.findCity(n, m, edges, distanceThreshold)
        print(ans)
