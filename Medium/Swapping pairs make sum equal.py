"""
Given two arrays of integers A[] and B[] of size N and M, the task is to check if a pair of values (one value from each array) exists such that swapping the elements of the pair will make the sum of two arrays equal.
"""

class Solution:
    def findSwapValues(self,a, n, b, m):
        sum_a = sum(a)
        sum_b = sum(b)
        
        if sum_b > sum_a:
            a, b = b, a
            sum_a, sum_b = sum_b, sum_a
            
        if (sum_a - sum_b) % 2 != 0:
            return -1
        
        diff = (sum_b - sum_a) // 2
        set_a = set(a)
        
        for bx in b:
            ax = bx - diff
            if ax in set_a:
                return 1
        return -1

if __name__ == '__main__': 
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        m=l[1]
        a = list(map(int,input().split()))
        b = list(map(int, input().split()))
        ob = Solution()
        print(ob.findSwapValues(a,n,b,m))
