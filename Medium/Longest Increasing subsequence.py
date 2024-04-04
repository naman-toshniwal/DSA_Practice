"""
Given an array of integers, find the length of the longest (strictly) increasing subsequence from the given array.
"""

from bisect import bisect_left
class Solution:
    def longestSubsequence(self,a,n):
        lis = []
        
        for i in a:
            if len(lis)==0 or i > lis[-1]:
                lis.append(i)
            else:
                l_bound = bisect_left(lis, i)
                lis[l_bound] = i
        return len(lis)

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        a = [ int(x) for x in input().split() ]
        ob=Solution()
        print(ob.longestSubsequence(a,n))
