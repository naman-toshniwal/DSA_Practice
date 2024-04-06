"""
Given an array of n positive integers. Find the sum of the maximum sum subsequence of the given array such that the integers in the subsequence are sorted in strictly increasing order i.e. a strictly increasing subsequence. 
"""

class Solution:
    def maxSumIS(self, arr, n):
        dp=[i for i in arr]
        
        for i in range(1,n):
            for j in range(i):
                if arr[i]>arr[j]:
                    dp[i]=max(dp[i],dp[j]+arr[i])
        
        return max(dp)

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.maxSumIS(Arr,n)
        print(ans)
