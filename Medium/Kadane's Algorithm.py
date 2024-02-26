"""
Given an array Arr[] of N integers. Find the contiguous sub-array(containing at least one number) which has the maximum sum and return its sum.
"""

class Solution:
    def maxSubArraySum(self,arr,N):
        maximum = float('-inf')
        sum = 0
        
        for i in range(N):
            sum += arr[i]
            
            if sum > maximum:
                maximum = sum
            if sum < 0:
                sum = 0
        return maximum

import math
def main():
        T=int(input())
        while(T>0):    
            n=int(input())
            arr=[int(x) for x in input().strip().split()]
            ob=Solution()
            print(ob.maxSubArraySum(arr,n))
            T-=1

if __name__ == "__main__":
    main()
