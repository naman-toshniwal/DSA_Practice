"""
You are given a connected undirected graph. Perform a Depth First Traversal of the graph.
Note: Use the recursive approach to find the DFS traversal of the graph starting from the 0th vertex from left to right according to the graph.
"""

class Solution:
    def dfs(self, curr_node):
        self.result.append(curr_node)
        
        for number in self.adj[curr_node]:
            if number not in self.visited:
                self.visited.add(number)
                self.dfs(number)
        
    def dfsOfGraph(self, V, adj):
        self.n_nodes = V
        self.adj = adj
        self.visited = set([0])
        self.result = []
        self.dfs(0)
        return self.result

if __name__ == '__main__':
    T=int(input())
    while T>0:
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
