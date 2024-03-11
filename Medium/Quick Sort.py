"""
Quick Sort is a Divide and Conquer algorithm. It picks an element as a pivot and partitions the given array around the picked pivot.
Given an array arr[], its starting position is low (the index of the array) and its ending position is high(the index of the array).

Note: The low and high are inclusive.

Implement the partition() and quickSort() functions to sort the array.
"""

class Solution:
    def quickSort(self,arr,low,high):
        if low < high:
            pi = self.partition(arr, low, high)
            self.quickSort(arr, low, pi-1)
            self.quickSort(arr, pi+1, high)
    
    def partition(self,arr,low,high):
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return (i + 1)

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().quickSort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()
