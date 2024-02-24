"""
Given an unsigned integer N. The task is to swap all odd bits with even bits. For example, if the given number is 23 (00010111), it should be converted to 43(00101011). Here, every even position bit is swapped with an adjacent bit on the right side(even position bits are highlighted in the binary representation of 23), and every odd position bit is swapped with an adjacent on the left side.
"""

class Solution:
    def swapBits(self,n):
        mod_even = (n << 1) & (0xaaaaaaaa)
        mod_odd = (n >> 1) & (0x55555555)
        
        return (mod_even + mod_odd)

import math

def main():    
    T=int(input())
    
    while(T>0):
        n=int(input())
        ob=Solution()
        print(ob.swapBits(n))
        T-=1

if __name__=="__main__":
    main()
