"""
Consider a rat placed at (0, 0) in a square matrix of order N * N. It has to reach the destination at (N - 1, N - 1). Find all possible paths that the rat can take to reach from source to destination. The directions in which the rat can move are 'U'(up), 'D'(down), 'L' (left), 'R' (right). Value 0 at a cell in the matrix represents that it is blocked and rat cannot move to it while value 1 at a cell in the matrix represents that rat can be travel through it.
Note: In a path, no cell can be visited more than one time. If the source cell is 0, the rat cannot move to any other cell.
"""

class Solution:
    def findPath(self, matrix, n):
        def dfs(i, j, path):
            if i == n - 1 and j == n - 1 and matrix[i][j] == 1:
                paths.append(path)
                return
            
            if 0 <= i < n and 0 <= j < n and matrix[i][j] == 1 and (i, j) not in visited:
                visited.add((i, j))
                dfs(i - 1, j, path + 'U')  # Up
                dfs(i + 1, j, path + 'D')  # Down
                dfs(i, j - 1, path + 'L')  # Left
                dfs(i, j + 1, path + 'R')  # Right
                visited.remove((i, j))

        paths = []
        visited = set()
        
        if matrix[0][0] == 1:
            dfs(0, 0, '')
        return paths

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
