"""
Given a number n, find the nth number in the Padovan Sequence.

A Padovan Sequence is a sequence which is represented by the following recurrence relation
P(n) = P(n-2) + P(n-3)
P(0) = P(1) = P(2) = 1

Note: Since the output may be too large, compute the answer modulo 10^9+7.
"""

class Solution:
    def padovanSequence(self, n):
        m=1000000007
        
        if n<=2:
            return 1
        else:
            a,b,c=1,1,1
            d=0
            
            for i in range(3,n+1):
                d=(a%m+b%m)%m
                a,b,c=b,c,d
                
        return d

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.padovanSequence(n))
