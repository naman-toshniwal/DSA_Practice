"""
Given an array arr of distinct elements of size N, the task is to rearrange the elements of the array in a zig-zag fashion so that the converted array should be in the below form: 

arr[0] < arr[1]  > arr[2] < arr[3] > arr[4] < . . . . arr[n-2] < arr[n-1] > arr[n]. 

NOTE: If your transformation is correct, the output will be 1 else the output will be 0. 
"""

class Solution:
    def zigZag(self, arr, n):
        flag = True
        
        for i in range(n-1):
            if flag and arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
            elif flag == False and arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
            
            flag = not flag
        
        return arr

import sys
def isZigzag(arr, n):
    f = 1

    for i in range(1, n):
        if f:
            if arr[i-1] > arr[i]:
                return 0
        else:
            if arr[i-1] < arr[i]:
                return 0
        f = f ^ 1

    return 1

t = int(input())
while t:
    n = int(input())
    arr = [int(x) for x in input().split()]
    ob = Solution()
    ob.zigZag(arr, n)
    check = isZigzag(arr, n)

    if check:
        print("1")
    else:
        print("0")

    t -= 1

sys.exit(0)
