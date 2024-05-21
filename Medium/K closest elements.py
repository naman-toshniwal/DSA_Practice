"""
Given a sorted array of unique elements in increasing order, arr[] of n integers, and a value x. Find the K closest elements to x in arr[].
Keep the following points in mind:

If x is present in the array, then it need not be considered.
If two elements have the same difference as x, the greater element is prioritized.
If sufficient elements are not present on the right side, take elements from the left and vice versa.
"""

from typing import List
from math import inf

class Solution:
    def printKClosest(self, arr: List[int], n: int, k: int, x: int) -> List[int]:
        def getDiff(index: int) -> int:
            if index < 0 or index >= n:
                return inf
            return abs(x - arr[index])
        
        def findIndex(findMin: bool) -> int:
            res = -1
            left, right = 0, n-1
            
            while left <= right:
                mid = left + (right - left) // 2
                     
                if arr[mid] < x or (arr[mid] == x and findMin):
                    if findMin:
                        res = mid
                    left = mid + 1
                else:
                    if not findMin:
                        res = mid
                    right = mid - 1
            
            if arr[res] == x:
                res += -1 if findMin else 1
            return res
        leftIndex, rightIndex = findIndex(True), findIndex(False)
        res = []
        
        while leftIndex >= 0 or rightIndex < n:
            if len(res) == k:
                break
            leftDiff, rightDiff = getDiff(leftIndex), getDiff(rightIndex)
            
            if leftDiff < rightDiff:
                res.append(arr[leftIndex])
                leftIndex -= 1
            else:
                res.append(arr[rightIndex])
                rightIndex += 1
        
        return res

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        k, x = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.printKClosest(arr, n, k, x)
        for xx in ans:
            print(xx, end=" ")
        print()
        tc -= 1
