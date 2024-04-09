"""
Given a Directed Acyclic Graph (DAG) with V vertices and E edges, Find any Topological Sorting of that Graph.
"""

class Solution:
    def topoSort(self, V, adj):
        def dfs(node,visited,ans,adj):
            visited[node] = 1
            
            for i in adj[node]:
                if visited[i] == 0:
                    dfs(i,visited,ans,adj)
            
            ans.append(node)
        visited = [0 for _ in range(V)]
        ans = []
        
        for i in range(V):
            if visited[i] == 0:
                dfs(i,visited,ans,adj)

        return ans[::-1]

import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
    if N!=len(res):
        return False
    map=[0]*N
    for i in range(N):
        map[res[i]]=i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        e,N = list(map(int, input().strip().split()))
        adj = [[] for i in range(N)]
        
        for i in range(e):
            u,v=map(int,input().split())
            adj[u].append(v)
            
        ob = Solution()
        
        res = ob.topoSort(N, adj)
        
        if check(adj, N, res):
            print(1)
        else:
            print(0)
