"""
Given a weighted, undirected and connected graph of V vertices and an adjacency list adj where adj[i] is a list of lists containing two integers where the first integer of each list j denotes there is edge between i and j , second integers corresponds to the weight of that  edge . You are given the source vertex S and You to Find the shortest distance of all the vertex's from the source vertex S. You have to return a list of integers denoting shortest distance between each node and Source vertex S.
 

Note: The Graph doesn't contain any negative weight cycle.
"""

from collections import defaultdict
import heapq
import math

class Solution:
    def dijkstra(self, V, adj, S):

        graph = defaultdict(list)
        weight = defaultdict()
        
        for i in range(len(adj)):
            edges = adj[i]
            
            for edge in edges:
                nei, wt = edge
                
                graph[i].append(nei)
                weight[(i, nei)] = wt
        
        minHeap = []
        heapq.heapify(minHeap)
        heapq.heappush(minHeap, (0, S))
        distance = [math.inf] * V
        distance[S] = 0
        
        while minHeap:
            wt, node = heapq.heappop(minHeap)
            
            for nei in graph[node]:
                nei_wt = weight[(node, nei)]
                new_wt = wt + nei_wt
                
                if new_wt < distance[nei]:
                    distance[nei] = new_wt
                    heapq.heappush(minHeap, (new_wt, nei))
        
        return distance

import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
