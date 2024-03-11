"""
Given an array arr[], its starting position l and its ending position r. Sort the array using merge sort algorithm.
"""

class Solution:
    def merge(self,arr, l, m, r): 
        if l < m:
            arr1 = self.merge(arr, l, (l+m)//2, m)
            arr2 = self.merge(arr, m, (m+r)//2, r)
            i = j = 0
            temp = []
        
            while i < len(arr1) and j < len(arr2):
                if arr1[i] < arr2[j]:
                    temp.append(arr1[i])
                    i += 1
                else:
                    temp.append(arr2[j])
                    j += 1
        
            while i < len(arr1):
                temp.append(arr1[i])
                i += 1
        
            while j < len(arr2):
                temp.append(arr2[j])
                j += 1
        
            for i in range(l, r):
                arr[i] = temp[i - l]
            
            return temp
        else:
            return [arr[l]]
        
    def mergeSort(self,arr, l, r):
        if len(arr) == 1:
            pass
        elif len(arr) == 2:
            temp = [min(arr[0], arr[1]), max(arr[0], arr[1])]
            arr[0] = temp[0]
            arr[1] = temp[1]
        else:
            mid = (l + r) // 2
            self.merge(arr, l, mid, r+1)

import sys
input = sys.stdin.readline
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().mergeSort(arr, 0, n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()
