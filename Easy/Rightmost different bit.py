"""
Given two numbers M and N. The task is to find the position of the rightmost different bit in the binary representation of numbers. If both M and N are the same then return -1 in this case.
"""

import math

class Solution:
    def posOfRightMostDiffBit(self,m,n):
        if (m == n):
            return -1
        count = 1
        
        while True:
            if ((m & 1)^(n & 1) == 1):
                return count
            m >>= 1
            n >>= 1
            count += 1

def main():
    T=int(input())
    
    while(T>0):
        mn=[int(x) for x in input().strip().split()]
        m=mn[0]
        n=mn[1]
        ob=Solution()
        print(math.floor(ob.posOfRightMostDiffBit(m,n)))        
        T-=1

if __name__=="__main__":
    main()
