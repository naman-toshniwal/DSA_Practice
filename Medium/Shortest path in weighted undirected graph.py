"""
You are given a weighted undirected graph having n vertices numbered from 1 to n and m edges along with their weights. Find the shortest path between the vertex 1 and the vertex n,  if there exists a path, and return a list of integers whose first element is the weight of the path, and the rest consist of the nodes on that path. If no path exists, then return a list containing a single element -1.

The input list of edges is as follows - {a, b, w}, denoting there is an edge between a and b, and w is the weight of that edge.

Note: The driver code here will first check if the weight of the path returned is equal to the sum of the weights along the nodes on that path, if equal it will output the weight of the path, else -2. In case the list contains only a single element (-1) it will simply output -1. 
"""

from typing import List
from collections import defaultdict, deque
from heapq import heappush, heappop

class Solution:
    def shortestPath(self,n:int, m:int, edges:List[List[int]] )->List[int]:
        g = defaultdict(list)
        
        for frm, to, w in edges:
            g[frm].append((to, w))
            g[to].append((frm, w))
        
        q = [(0, 1)]
        costs = {1: 0}
        parents = {1: None}

        def build_path(cost, last):
            nonlocal parents
            q = deque()
            
            while last:
                q.appendleft(last)
                last = parents[last]
            q.appendleft(cost)
            return q
            
        while q:
            cost0, frm = heappop(q)
            
            if frm == n:
                return build_path(cost0, frm)
            
            for to, w in g[frm]:
                cost = cost0+w
                if to not in costs or cost < costs[to]:
                    costs[to] = cost
                    parents[to] = frm
                    heappush(q, (cost, to))
                    
        return [-1]

from collections import defaultdict
def check(n, path, edges):
    gp = [{} for i in range(n + 1)]
    for u, v, w in edges:
        if v in gp[u]:
            gp[u][v] = min(gp[u][v], w)
        else:
            gp[u][v] = w

        if u in gp[v]:
            gp[v][u] = min(gp[v][u], w)
        else:
            gp[v][u] = w

    s = 0
    for i in range(2, len(path)):
        if path[i] not in gp[path[i - 1]]:
            return False
        s += gp[path[i - 1]][path[i]]

    return s == path[0]

if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().split())
        edges = []
        for i in range(m):
            a, b, w = map(int, input().split())
            edges.append([a, b, w])

        obj = Solution()
        res = obj.shortestPath(n, m, edges)
        if res[0] == -1:
            print(-1)
        else:
            if check(n, res, edges):
                print(res[0])
            else:
                print(-2)
