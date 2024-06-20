"""
Given three non-collinear points whose co-ordinates are p(p1, p2), q(q1, q2) and r(r1, r2) in the X-Y plane. Return the number of integral / lattice points strictly inside the triangle formed by these points.
Note: - A point in the X-Y plane is said to be an integral / lattice point if both its coordinates are integral.
"""

from math import gcd

class Solution:
    def gcd(self, a, b):
        if b==0:
            return a
        else:
            return self.gcd(b, a%b)
            
    def linePoint(self, x1, y1, x2, y2):
        if x1==x2:
            return abs(y2-y1) -1
            
        if y1==y2:
            return abs(x2-x1)-1
        return self.gcd(abs(x1-x2), abs(y1-y2)) - 1
        
        
    def InternalCount(self, p, q, r):
        x1, y1 = p
        x2, y2 = q
        x3, y3 = r

        points = self.linePoint(x1, y1, x2, y2) + self.linePoint(x2, y2, x3, y3) + self.linePoint(x3, y3, x1, y1) + 3
        area = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
        return (area - points + 2) // 2

import math      
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        p=[0]*2
        q=[0]*2
        r=[0]*2
        p[0],p[1],q[0],q[1],r[0],r[1]=map(int,input().strip().split(" "))
        ob=Solution()
        ans=ob.InternalCount(p,q,r);
        print(ans)
