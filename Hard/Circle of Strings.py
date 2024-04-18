"""
Given an array of lowercase strings A[] of size N, determine if the strings can be chained together to form a circle.
A string X can be chained together with another string Y if the last character of X is same as first character of Y. If every string of the array can be chained with exactly two strings of the array(one with the first character and second with the last character of the string), it will form a circle.

For example, for the array arr[] = {"for", "geek", "rig", "kaf"} the answer will be Yes as the given strings can be chained as "for", "rig", "geek" and "kaf"
"""

from collections import defaultdict

class Solution:
    def isCircle(self, N, A):
        graph = defaultdict(list)
        mark = [0] * 26
        indegree = [0] * 26
        outdegree = [0] * 26
        vis = [0] * 26

        for i in range(N):
            s = A[i]
            u = ord(s[0]) - 97
            v = ord(s[len(s) - 1]) - 97
            indegree[u] += 1
            outdegree[v] += 1
            mark[u] = 1
            mark[v] = 1
            graph[u].append(v)

        def dfs(root):
            vis[root] = 1

            for node in graph[root]:
                if vis[node] == 0:
                    dfs(node)

        def safe(s):
            dfs(s)

            for i in range(26):
                if vis[i] == 0 and mark[i] == 1 : return False
            return True

        for i in range(26) :
            if (indegree[i] != outdegree[i]):
                return 0

        if (safe(ord(A[0][0]) - 97) == True):
            return 1
        return 0

import sys
sys.setrecursionlimit(10**6)
if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        A = input().split()
        ob = Solution()
        print(ob.isCircle(N, A))
