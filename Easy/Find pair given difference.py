"""
Given an array arr[] of size n and an integer x, return 1 if there exists a pair of elements in the array whose absolute difference is x, otherwise, return -1.
"""

from typing import List

class Solution:
    def findPair(self, n: int, x: int, arr: List[int]) -> int:
        num_set = set(arr)
        
        for num in arr:
            if x != 0 and (x + num) in num_set:
                return 1
            elif x == 0 and arr.count(num) > 1:
                return 1
        
        return -1

class IntArray:
    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()] 
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        x = int(input())
        arr = IntArray().Input(n)
        obj = Solution()
        res = obj.findPair(n, x, arr)
        print(res)
