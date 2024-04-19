"""
Given two arrays a of size n and b of size m, the task is to find numbers which are present in the first array, but not present in the second array.
"""

class Solution:
    def findMissing(self, a, b, n, m):
        b_set = set(b)
        missing_elements = []
        
        for num in a:
            if num not in b_set:
                missing_elements.append(num)
        return missing_elements

t=int(input())
for _ in range(0,t):
    l = list(map(int, input().split()))
    n=l[0]
    m=l[1]
    a = list(map(int,input().split()))
    b = list(map(int, input().split()))
    ob=Solution()
    ans=ob.findMissing(a,b,n,m)
    for each in ans:
        print(each,end=' ')
    print()
