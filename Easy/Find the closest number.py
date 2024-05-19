"""
Given a sorted array arr[] of positive integers. The task is to find the closest value in the array to the given number k. The array may contain duplicate values.

Note: If the difference with k is the same for two values in the array return the greater value.
"""

from typing import List
import math

class Solution:
    def findClosest(self, n : int, k : int, arr : List[int]) -> int:
        low, high = 0, len(arr) - 1
        ans = -math.inf

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == k:
                return k

            if arr[mid] <= k:
                if ans == -math.inf or abs(ans - k) > abs(arr[mid] - k):
                    ans = arr[mid]
                low = mid + 1
            else:
                if ans == -math.inf or abs(ans - k) >= abs(arr[mid] - k):
                    ans = arr[mid]
                high = mid - 1

        return ans

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
        k = int(input())     
        arr=IntArray().Input(n)
        obj = Solution()
        res = obj.findClosest(n, k, arr)        
        print(res)
