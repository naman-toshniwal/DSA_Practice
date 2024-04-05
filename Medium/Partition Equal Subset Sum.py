"""
Given an array arr[] of size N, check if it can be partitioned into two parts such that the sum of elements in both parts is the same.
"""

class Solution:
    def equalPartition(self, N, arr):
        total=sum(arr)
       
        if total %2 ==1:
            return 0
        target= total//2
        dp=[0]*(target+1)
        dp[0]=1
        
        for i in arr:
            achieved=set()
            
            for j in range(i,target+1):
                if dp[j]==0 and dp[j-i] and (j-i) not in achieved:
                    dp[j]=1
                    achieved.add(j)
                
                if dp[-1]:
                    return 1
       
        return 0

import sys
input = sys.stdin.readline
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])
        
        ob = Solution()
        if (ob.equalPartition(N, arr) == 1):
            print("YES")
        else:
            print("NO")
