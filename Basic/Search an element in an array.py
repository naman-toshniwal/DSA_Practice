"""
Given an integer array and another integer element. The task is to find if the given element is present in array or not.
"""

class Solution:
    def search(self,arr, N, X):
        flag=0
        
        for i in range(N):
            if arr[i] == X:
                return i
                flag=1
                
        if flag!=1:
            return -1

import math
def main():
        T=int(input())
        while(T>0):
            N=int(input())
            A=[int(x) for x in input().strip().split()]
            x=int(input())
            ob=Solution()
            print(ob.search(A,N,x))
            T-=1

if __name__ == "__main__":
    main()
