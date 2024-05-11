"""
Juggler Sequence is a series of integers in which the first term starts with a positive integer number a and the remaining terms are generated from the immediate previous term using the below recurrence relation:

Juggler Formula

Given a number n, find the Juggler Sequence for this number as the first term of the sequence until it becomes 1.
"""

class Solution:
    def jugglerSequence(self, n):
        l=[n]
        
        while n>1:
            if n%2!=0:
                c=int(n**(1.5))
                l.append(c)
                n=c
            else:
                d=int(n**(0.5))
                l.append(d)
                n=d
                
        return l

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        arr = ob.jugglerSequence(n)
        for i in (arr):
            print(i, end=" ")
        print()
