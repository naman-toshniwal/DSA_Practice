"""
You are given two numbers A and B. The task is to count the number of bits needed to be flipped to convert A to B.
"""

class Solution:
    def countBitsFlip(self,a, b):
        xor_result = a ^ b
        count = 0
        
        while xor_result:
            count += xor_result & 1
            xor_result >>= 1
        return count

import math
def main():
    T=int(input())
    
    while(T>0):
        ab=[int(x) for x in input().strip().split()]
        a=ab[0]
        b=ab[1]
        ob=Solution()
        print(ob.countBitsFlip(a,b))
        T-=1

if __name__=="__main__":
    main()
