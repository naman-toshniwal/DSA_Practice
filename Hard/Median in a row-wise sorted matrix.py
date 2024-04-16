"""
Given a row wise sorted matrix of size R*C where R and C are always odd, find the median of the matrix.
"""

class Solution:
    def countEleSmallerEqualToMid(self, arr, m, mid):
        low = 0
        high = m - 1
        
        while low <= high:
            mid_ = (low + high) // 2
            if arr[mid_] <= mid:
                low = mid_ + 1
            else:
                high = mid_ - 1
        return low

    def median(self, arr, n, m):
        low = 1
        high = 2000
        
        while low <= high:
            mid = (low + high) // 2
            cnt = sum(self.countEleSmallerEqualToMid(row, m, mid) for row in arr)
            if cnt <= ((n * m) // 2):
                low = mid + 1
            else:
                high = mid - 1
        return low

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        r,c = map(int,input().strip().split())
        matrix = [[0 for j in range(c)] for i in range(r)]
        for i in range(r):
            t=[int(el) for el in input().split()]
            for j in range(c):
                matrix[i][j]=t[j]
        ans = ob.median(matrix, r, c);
        print(ans)
