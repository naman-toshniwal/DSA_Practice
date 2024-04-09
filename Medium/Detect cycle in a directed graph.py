"""
Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, check whether it contains any cycle or not.
"""

class Solution:
    def isCyclic(self, V, adj):
        vis_arr = [0 for i in range(V)]
        path_vis = [0 for i in range(V)]
        
        for i in range(V):
            if vis_arr[i]==0:
                if self.dfs(vis_arr,path_vis,i,adj,V)==True:
                    return True
       
        return False
    
    def dfs(self,vis_arr,path_vis,i,adj,V):
        vis_arr[i]=1
        path_vis[i]=1
        
        for j in adj[i]:
            if vis_arr[j]==0:
                vis_arr[j]=1
                path_vis[j]=1
                if self.dfs(vis_arr,path_vis,j,adj,V)==True:
                    return True
                path_vis[j]=0
            
            else:
                if path_vis[j]==1:
                    return True
        
        path_vis[i]=0
        return 

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
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
