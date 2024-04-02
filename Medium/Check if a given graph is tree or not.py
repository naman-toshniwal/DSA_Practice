"""
You are given an undirected graph of N nodes (numbered from 0 to N-1) and M edges. Return 1 if the graph is a tree, else return 0.

Note: The input graph can have self-loops and multiple edges.
"""

class Solution:
    def isCyclePresent(self,node,adj,vis,p):
        vis.add(node)
        
        for i in adj[node]:
            if i not in vis:
                if not self.isCyclePresent(i,adj,vis,node): 
                    return 0
            
            elif i!=p: 
                return 0
        
        return 1
    
    def isTree(self, n, m, edges):
        adj,vis=[[]for _ in range(n)],set()
        
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
        
        b=self.isCyclePresent(0,adj,vis,-1)
        if len(vis)!=n: return 0
        return b

for _ in range (int(input())):
    n,m = [int(i) for i in input().split()]
    edges = []
    for i in range(m):
        a,b = map(int,input().split())
        edges.append([a,b])

    ob = Solution()
    print(ob.isTree(n,m,edges))
