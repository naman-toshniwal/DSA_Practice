"""
Given a number N. The task is to check whether it is sparse or not. A number is said to be a sparse number if no two or more consecutive bits are set in the binary representation.
"""

class Solution:
    def isSparse(self,n):
        if (n & (n >> 1)):
            return 0
        return 1

import math
def main():
    T=int(input())
    
    while(T>0):
        n=int(input())
        ob=Solution()
        if ob.isSparse(n):
            print("1")
        else:
            print("0")
        T-=1

if __name__=="__main__":
    main()
