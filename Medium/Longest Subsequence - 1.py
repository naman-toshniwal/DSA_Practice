"""
Given an integer array a[] of size n, find the length of the longest subsequence such that the absolute difference between adjacent elements is 1.
"""

from typing import List

class Solution:
    def longestSubseq(self, n : int, a : List[int]) -> int:
        ans, dp = 0, [0]*n
        
        for i in range(1, n):
            for j in range(0, i):
                if abs(a[i]-a[j]) == 1:
                    dp[i] = max(dp[i], dp[j]+1)
            
            ans = max(ans, dp[i])
        return ans+1

class IntArray:
    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = IntArray().Input(n)
        obj = Solution()
        res = obj.longestSubseq(n, a)
        print(res)
