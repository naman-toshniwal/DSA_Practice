"""
A matrix is constructed of size n*n and given an integer ‘q’. The value at every cell of the matrix is given as, M(i,j) = i+j, where ‘M(i,j)' is the value of a cell, ‘i’ is the row number, and ‘j’ is the column number. Return the number of cells having value ‘q’.

Note: Assume, the array is in 1-based indexing.
"""

class Solution:
    def sumMatrix(self, n, q):
        mid = n+1
        
        if  q in range(2, 2*n+1):
            if q == mid  :
                return n
            elif q < mid :
                return (q-1 )
            else:  
                return (2*n - q +1 )
        else : return 0 

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())

        ob = Solution()
        print(ob.sumMatrix(n, q))
