"""
Given a non-negative number n and two values l and r. The problem is to toggle the bits in the range l to r in the binary representation of n, i.e., to toggle bits from the lth least significant bit to the rth least significant bit (the rightmost bit as counted as the first bit).

A toggle operation flips a bit 0 to 1 and a bit 1 to 0.
"""

class Solution:
    def toggleBits(self, n , l , r):
        a=1
        a=a<<l-1
        
        while(l<=r):
            if(n&a==0):
                n=n+2**(l-1)
            else:
                n=n-2**(l-1)
            l=l+1
            a=a<<1
        return n

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n,l,r=map(int,input().split())
        
        ob = Solution()
        print(ob.toggleBits(n,l,r))
