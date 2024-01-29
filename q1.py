"""
Given an array of size N-1 such that it only contains distinct integers in the range of 1 to N. Find the missing element.
"""

class Solution:
    def missingNumber(self,array,n):
        total_sum = n*(n+1)//2
        arr_sum = sum(array)
        missing = total_sum - arr_sum
        return missing

t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().missingNumber(a,n)
    print(s)
