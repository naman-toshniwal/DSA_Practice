"""
Given two arrays a and b of positive integers of size n and m where n >= m, the task is to maximize the dot product by inserting zeros in the second array but you cannot disturb the order of elements.

Dot product of array a and b of size n is a[0]*b[0] + a[1]*b[1] + ... + a[n-1]*b[n-1].
"""

class Solution:
    def maxDotProduct(self, n, m, a, b):
        dp = [[0]*(m+1) for _ in range(n+1)]
        
        for i in range(n):
            for j in range(min(m, i+1)):
                dp[i+1][j+1] = max(dp[i][j] + a[i]*b[j], dp[i][j+1])
        
        return dp[n][m]

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n,m = input().split()
        n,m = int(n),int(m)
        a = [int(x) for x in input().split()]
        b = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.maxDotProduct(n,m,a,b)
        print(ans)
