"""
Given an array A of n non negative numbers. The task is to find the first equilibrium point in an array. Equilibrium point in an array is an index (or position) such that the sum of all elements before that index is same as sum of elements after it.

Note: Return equilibrium point in 1-based indexing. Return -1 if no such point exists. 
"""

class Solution:
    def equilibriumPoint(self,A, N):
        total_sum = sum(A)
        left_sum = 0
        
        for i in range(N):
            right_sum = total_sum - A[i] - left_sum
            
            if left_sum == right_sum:
                return (i+1)
            
            left_sum += A[i]
        
        return -1

import math
def main():
    T = int(input())

    while(T > 0):
        N = int(input())
        A = [int(x) for x in input().strip().split()]
        ob=Solution()
        print(ob.equilibriumPoint(A, N))

        T -= 1

if __name__ == "__main__":
    main()