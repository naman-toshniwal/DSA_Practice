"""
Given an unsorted array A of size N that contains only non negative integers, find a continuous sub-array that adds to a given number S and return the left and right index(1-based indexing) of that subarray.

In case of multiple subarrays, return the subarray indexes which come first on moving from left to right.

Note:- You have to return an ArrayList consisting of two elements left and right. In case no such subarray exists return an array consisting of element -1.
"""

class Solution:
    def subArraySum(self,arr, n, s): 
        start = 0
        current_sum = 0
       
        for i in range(n):
            current_sum += arr[i]
           
            while (current_sum > s and start < i):
                current_sum -= arr[start]
                start += 1
            
            if (current_sum == s):
                return [start + 1, i + 1]
        
        return [-1]

import math
def main():
        T=int(input())
        while(T>0):          
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])          
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")               
            print()
            T-=1

if __name__ == "__main__":
    main()
