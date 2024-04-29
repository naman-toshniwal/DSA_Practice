"""
Given a sorted array arr[] of distinct integers. Sort the array into a wave-like array(In Place).
In other words, arrange the elements into a sequence such that arr[1] >= arr[2] <= arr[3] >= arr[4] <= arr[5].....

If there are multiple solutions, find the lexicographically smallest one.

Note:The given array is sorted in ascending order, and you don't need to return anything to make changes in the original array itself.
"""

from typing import List

class Solution:
    def convertToWave(self, n : int, a : List[int]) -> None:
        for i in range(0, n-1, 2):
            a[i], a[i+1] = a[i+1], a[i]

class IntArray:
    def __init__(self) -> None:
        pass

    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]
        return arr
    
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a=IntArray().Input(n)
        obj = Solution()
        obj.convertToWave(n, a)
        IntArray().Print(a)
