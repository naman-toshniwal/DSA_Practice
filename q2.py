"""
Given an array A of positive integers. Your task is to find the leaders in the array. An element of array is a leader if it is greater than or equal to all the elements to its right side. The rightmost element is always a leader. 
"""

class Solution:
    def leaders(self, A, N):
        max_right = A[N-1]        
        leaders = [max_right]
        
        for i in range(N-2, -1, -1):
            if A[i] >= max_right:
                max_right = A[i]
                leaders.insert(0, max_right)
        
        return leaders

import math    
def main():   
    T=int(input())

    while(T>0):        
        N=int(input())       
        A=[int(x) for x in input().strip().split()]
        obj = Solution()       
        A=obj.leaders(A,N)
        
        for i in A:
            print(i,end=" ")
        print()
                
        T-=1

if __name__=="__main__":
    main()