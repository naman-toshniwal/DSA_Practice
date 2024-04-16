"""
You are given an array arr of size n. You have to remove a subarray of size k , such that the difference between the maximum and minimum values of the remaining array is minimized.
Find the minimum value obtained after performing the operation of the removal of the subarray and return it.
"""

from typing import List

class Solution:
    def minimizeDifference(self, n : int, k : int, arr : List[int]) -> int:
        premax = arr.copy()
        premin = arr.copy()
        sufmax = arr.copy()
        sufmin = arr.copy()
        
        for i in range(1,n):
            premax[i] = max(arr[i], premax[i-1])
            premin[i] = min(arr[i], premin[i-1])
        
        for i in range(n-2, -1 , -1):
            sufmax[i] = max(arr[i], sufmax[i+1])
            sufmin[i] = min(arr[i], sufmin[i+1])
        
        res = max(arr)
        res = min(res, sufmax[k]-sufmin[k])
        
        for i in range(1,n-k):
            res = min(res, max(premax[i-1],sufmax[i+k])-min(premin[i-1],sufmin[i+k]))
        res = min(res, premax[n-k-1]-premin[n-k-1])
        return res

class IntArray:
    def __init__(self) -> None:
        pass
    
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        k = int(input())
        arr=IntArray().Input(n)
        obj = Solution()
        res = obj.minimizeDifference(n, k, arr)
        print(res)
