"""
Given an integer number n, which is a decimal representation of Gray Code. Find the binary equivalent of the Gray Code & return the decimal representation of the binary equivalent.
"""

class Solution:    
    def grayToBinary(self,n):
        ans=0

        while n:
            ans^=n
            n>>=1
        return ans

import math
def main():
    T=int(input())
    
    while(T>0): 
        n=int(input())
        ob=Solution()
        print(ob.grayToBinary(n))
        T-=1

if __name__=="__main__":
    main()
