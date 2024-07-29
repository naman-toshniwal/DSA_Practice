"""
Given a boolean 2D array, consisting of only 1's and 0's, where each row is sorted. Find the 0-based index of the first row that has the maximum number of 1's. Return the 0-based index of the first row that has the most number of 1s. If no such row exists, return -1.
"""

class Solution:
    def rowWithMax1s(self, arr):
        max_ = 0
        index = -1
        
        for i in range(len(arr)):
            count = arr[i].count(1)
            
            if(max_ < count):
                max_ = count 
                index = i 
                
        return index

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))
        inputLine = list(map(int, input().strip().split()))
        arr = [[0 for j in range(m)] for i in range(n)]

        for i in range(n):
            for j in range(m):
                arr[i][j] = inputLine[i * m + j]
        ob = Solution()
        ans = ob.rowWithMax1s(arr)
        print(ans)
        tc -= 1
