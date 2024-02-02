"""
Given a boolean 2D array, where each row is sorted. Find the row with the maximum number of 1s.
"""

class Solution:
    def maxOnes (self, Mat, N, M):
        max, count = 0, 0
        for i in range(N):
            count_1 = 0
            
            for j in range(M):
                if (Mat[i][j] == 1):
                    count_1 += 1
            
            if count_1 > max:
                max = count_1
                count = i
            
        return count

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        size = input().strip().split()
        r = int(size[0])
        c = int(size[1])
        line = list(map(int,input().split()))
        matrix = [ [0 for _ in range(c)] for _ in range(r) ]
        for i in range(r):
            for j in range(c):
                matrix[i][j] = line[i*c+j]
        ob = Solution()
        print(ob.maxOnes(matrix,r,c))
