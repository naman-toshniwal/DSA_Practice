"""
Given an undirected graph with v vertices(numbered from 1 to v) and e edges. Find the number of good components in the graph.
A component of the graph is good if and only if the component is fully connected.
Note: A fully connected component is a subgraph of a given graph such that there's an edge between every pair of vertices in the component, the given graph can be a disconnected graph. 
"""

from typing import List
from collections import defaultdict

class Solution:
    def findNumberOfGoodComponent(self, e : int, v : int, edges : List[List[int]]) -> int:
        parent = list(range(v))
        
        def find(x: int) -> int: 
            if parent[x]==x: return x
            parent[x] = find(parent[x])
            return parent[x]
        degree = [0]*v
        
        for x,y in edges:
            degree[x-1] += 1
            degree[y-1] += 1
            parent[find(x-1)] = find(y-1)
        group = defaultdict(list)
        
        for i in range(v): 
            group[find(i)].append(i)
        return sum(all(degree[x]==len(comps)-1 for x in comps) for comps in group.values())

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
        e = int(input())
        v = int(input())
        edges = IntMatrix().Input(e, 2)
        obj = Solution()
        res = obj.findNumberOfGoodComponent(e, v, edges)
        print(res)
