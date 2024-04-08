"""
Given an undirected graph with V vertices labelled from 0 to V-1 and E edges, check whether it contains any cycle or not. Graph is in the form of adjacency list where adj[i] contains all the nodes ith node is having edge with.
"""

from typing import List

class Solution:
    def bfs(self,v,adj,n,p):
        q=[]
        v[n]=1
        q.append([n,p])

        while len(q):
            a=q.pop(0)
            Node=a[0]
            Parent=a[1]

            for i in adj[Node]:
                if not v[i]:
                    v[i]=1
                    q.append([i,Node])
                elif v[i] and i!=Parent:
                    return True

        return False

    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        v=[0]*V
        
        for Node in range(V):
            if not v[Node]:
                if self.bfs(v,adj,Node,-1):
                    return True
        
        return False

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
        ans = obj.isCycle(V, adj)
        if(ans):
            print("1")
        else:
            print("0")
