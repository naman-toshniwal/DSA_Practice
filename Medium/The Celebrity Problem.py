"""
A celebrity is a person who is known to all but does not know anyone at a party. A party is being organized by some people.  A square matrix mat is used to represent people at the party such that if an element of row i and column j is set to 1 it means ith person knows jth person. You need to return the index of the celebrity in the party, if the celebrity does not exist, return -1.

Note: Follow 0-based indexing.
"""

class Solution:
    def celebrity(self, mat):
        n = len(mat)
        
        for i, k in enumerate(mat):
            if sum(k) == 0 and sum([mat[j][i] for j in range(n)]) == n-1:
                return i
        
        return -1

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        M = []
        for _ in range(n):
            M.append(list(map(int, input().split())))
        ob = Solution()
        print(ob.celebrity(M))
