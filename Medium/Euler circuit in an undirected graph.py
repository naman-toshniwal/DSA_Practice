"""
Eulerian Path is a path in a graph that visits every edge exactly once. Eulerian Circuit is an Eulerian Path that starts and ends on the same vertex. Given the number of vertices v and adjacency list adj denoting the graph. Find that there exists the Euler circuit or not. Return 1 if there exist  alteast one eulerian path else 0.
"""

class Solution:
    def isEularCircuitExist(self, v, adj):
        for i in range(v):
            if len(adj[i])%2!=0:
                return 0
        return 1

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        V, E = map(int, input().split())
        adj = [[] for i in range(V)]
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
        obj = Solution()
        ans = obj.isEularCircuitExist(V, adj)
        if(ans):
            print("1")
        else:
            print("0")
