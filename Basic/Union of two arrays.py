"""
Given two arrays a[] and b[] of size n and m respectively. The task is to find the number of elements in the union between these two arrays.

Union of the two arrays can be defined as the set containing distinct elements from both the arrays. If there are repetitions, then only one occurrence of element should be printed in the union.

Note : Elements are not necessarily distinct.
"""

class Solution:
    def doUnion(self,a,n,b,m):
        a = set(a)
        b = set(b)
        arr = a.union(b)
        return(len(arr))

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n,m=[int(x) for x in input().strip().split()]
        a=[int(x) for x in input().strip().split()]
        b=[int(x) for x in input().strip().split()]
        ob=Solution()
        print(ob.doUnion(a,n,b,m))
