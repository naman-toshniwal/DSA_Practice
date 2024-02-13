"""
Given a number N. Find the length of the longest consecutive 1s in its binary representation.
"""

class Solution:
    def maxConsecutiveOnes(self, N):
        maxx = 0
        count = 0
        
        while N > 0:
            if (N % 2 == 1):
                count += 1
                maxx = max(maxx, count)
            else:
                count = 0
            N //= 2
        
        return maxx

import math

def main():   
    T=int(input())
    
    while(T>0):      
        n=int(input())
        obj = Solution()
        print(obj.maxConsecutiveOnes(n))
        T-=1

if __name__=="__main__":
    main()
