"""
Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, Find the number of strongly connected components in the graph.
"""

class Solution:
    def kosaraju(self, V, adj):
        rev = [[] for _ in range(V)]
        stack = []
        visited = [0]*V
        
        def dfs(node ,graph):
            if visited[node]:
                return 
            visited[node] = 1

            for ne in graph[node]:
                dfs(ne ,graph)
            stack.append(node)

        for i in range(V):
            dfs(i, adj)

        for i in range(V):
            for n in adj[i]:
                rev[n].append(i)
                
        ans = 0
        visited  = [0]*V
        
        while len(stack):
            node = stack.pop()
            if not visited[node]:
                ans+=1
                dfs(node,rev)

        return ans

from collections import OrderedDict 
import sys 
sys.setrecursionlimit(10**6) 
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()        
        print(ob.kosaraju(V, adj))
