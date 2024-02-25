"""
Given a directed graph. The task is to do Breadth First Traversal of this graph starting from 0.
Note: One can move from node u to node v only if there's an edge from u to v. Find the BFS traversal of the graph starting from the 0th vertex, from left to right according to the input graph. Also, you should only take nodes directly or indirectly connected from Node 0 in consideration.
"""

from typing import List
from queue import Queue
class Solution:
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        self.visited = []
        self.visited_queue = []
        
        if V == 1:
            return []
        self.bfs(0, adj)
        return self.visited
        
    def bfs(self, index, adj):
        self.visited.append(index)
        self.visited_queue.extend(adj[index])
        
        while self.visited_queue:
            j = self.visited_queue.pop(0)
            if j not in self.visited:
                self.bfs(j, adj)
        return

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        V, E = map(int, input().split())
        adj = [[] for i in range(V)]
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
        ob = Solution()
        ans = ob.bfsOfGraph(V, adj)
        for i in range(len(ans)):
            print(ans[i], end = " ")
        print()
