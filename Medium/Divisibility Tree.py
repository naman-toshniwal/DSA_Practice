"""
Given a tree with n nodes numbered from 1 to n and n - 1 edges connecting them. The tree is rooted at node 1. Your task is to remove a maximum number of edges from the given tree such that the tree converts into a disjoint union tree and the nodes of connected components left are divisible by 2. If n is odd, then it is allowed to keep exactly one component with an odd number of nodes. 
"""

from typing import List

class Solution:
    def dfs(self, adj: List[List[int]], u: int, prt: int, ans: List[int]) -> int:
        count = 0
        
        for v in adj[u]:
            if v != prt:
                x = self.dfs(adj, v, u, ans)
                
                if x % 2 == 0:
                    ans[0] += 1
                else:
                    count += x
                    
        return count + 1

    def minimumEdgeRemove(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        
        for edge in edges:
            adj[edge[1] - 1].append(edge[0] - 1)
            adj[edge[0] - 1].append(edge[1] - 1)

        ans = [0]
        self.dfs(adj, 0, -1, ans)
        return ans[0]

class IntMatrix:
    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        edges = IntMatrix().Input(n - 1, 2)
        obj = Solution()
        res = obj.minimumEdgeRemove(n, edges)
        print(res)
