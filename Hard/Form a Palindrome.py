"""
Given a string, find the minimum number of characters to be inserted to convert it to palindrome.
For Example:
ab: Number of insertions required is 1. bab or aba
aa: Number of insertions required is 0. aa
abcd: Number of insertions required is 3. dcbabcd
"""

class Solution:
    def countMin(self, s):
        n=len(s)
        dp=[[0]*(n) for i in range(n)]
        
        for i in range(n-1):
            if s[i]!=s[i+1]:
                dp[i][i+1]=1
        
        for i in range(n-1,-1,-1):
            for j in range(i+2,n):
                if s[i]!=s[j]:
                    dp[i][j]=min(1+dp[i+1][j],1+dp[i][j-1])
                else:
                    dp[i][j]=min(1+dp[i+1][j],1+dp[i][j-1],dp[i+1][j-1])
        
        return dp[0][n-1]

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        Str = input()
        solObj = Solution()
        print(solObj.countMin(Str))
