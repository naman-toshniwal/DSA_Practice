"""
The problem is to find the shortest distances between every pair of vertices in a given edge-weighted directed graph. The graph is represented as an adjacency matrix of size n*n. Matrix[i][j] denotes the weight of the edge from i to j. If Matrix[i][j]=-1, it means there is no edge from i to j.
Do it in-place.
"""

class Solution:
    def shortest_distance(self, matrix):
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if matrix[i][k] != -1 and matrix[k][j] != -1:
                        if matrix[i][j] == -1 or matrix[i][k] + matrix[k][j] < matrix[i][j]:
                            matrix[i][j] = matrix[i][k] + matrix[k][j]
        
        return matrix
 

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, input().split())))
        obj = Solution()
        obj.shortest_distance(matrix)
        for _ in range(n):
            for __ in range(n):
                print(matrix[_][__], end = " ")
            print()
