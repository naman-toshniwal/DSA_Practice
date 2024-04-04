"""
Given two strings, find the length of longest subsequence present in both of them. Both the strings are in uppercase latin alphabets.
"""

class Solution:
    def lcs(self,x,y,s1,s2):
        dp = [[0]*(y+1) for i in range(x+1)]
        
        for i in range(1,x+1):
            for j in range(1, y+1):
                if s1[i-1]==s2[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
        return dp[x][y]

import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        x,y = map(int,input().strip().split())
        s1 = str(input())
        s2 = str(input())
        ob=Solution()
        print(ob.lcs(x,y,s1,s2))
