"""
Given an integer N. The task is to return the position of first set bit found from the right side in the binary representation of the number.
Note: If there is no set bit in the integer N, then return 0 from the function.  
"""

import math

class Solution:
    def getFirstSetBit(self,n):
        if n == 0:
            return 0
        position = 1
        
        while n > 0:
            if n % 2 == 1:
                return position
            n = n // 2
            position += 1
        
        return 0

def main():
    T=int(input())
    
    while(T>0):
        n=int(input())
        ob=Solution()
        print(ob.getFirstSetBit(n))        
        T-=1

if __name__=="__main__":
    main()