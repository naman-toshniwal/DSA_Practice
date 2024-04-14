"""
You are given an array arr[] of size n. You need to do the following:

1. You need to calculate the bitwise XOR of each element in the array with its corresponding index (indices start from 0).
2. After step1, print the array.
3. Now, set all the elements of arr[] to zero.
4. Now, print arr[].
"""

class Solution:
    def printArr(self, n, arr):
        return 

    def setToZero(self, n, arr):
        ans = [0]*n
        for i  in range(n):
            if i == n-1 : 
                print(ans[i])
            else: 
                print(ans[i] , end=" ")
            

    def xor1ToN(self, n, arr):
        x=[arr[i]^(i) for i in range(n)]
        for i in range(n):
            if i == n-1 : 
                print(x[i])
            else: 
                print(x[i] , end=" ")

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        obj = Solution()
        obj.xor1ToN(n, arr)
        obj.printArr(n, arr)
        obj.setToZero(n, arr)
        obj.printArr(n, arr)
