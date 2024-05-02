"""
Given an 0-indexed array of integers arr[] of size n, find its peak element and return it's index. An element is considered to be peak if it's value is greater than or equal to the values of its adjacent elements (if they exist).

Note: The output will be 1 if the index returned by your function is correct; otherwise, it will be 0.
"""

class Solution:   
    def peakElement(self,arr, n):
        return self.findPeakUtil(arr, 0, n - 1, n)
    
    def findPeakUtil(self,arr,low, high,n):
        mid = low + (high - low)/2
        mid = int(mid)

        if ((mid == 0 or arr[mid - 1] <= arr[mid]) and
            (mid == n - 1 or arr[mid + 1] <= arr[mid])):
            return mid
    
        elif (mid > 0 and arr[mid - 1] > arr[mid]):
            return self.findPeakUtil(arr, low, (mid - 1), n)
    
        else:
            return self.findPeakUtil(arr, (mid + 1), high, n)

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        index = Solution().peakElement(arr.copy(), n)
        flag = False
        if index<0 or index>=n:
            flag = False
        else:
            if index == 0 and n==1:
                flag = True
            elif index==0 and arr[index]>=arr[index+1]:
                flag = True
            elif index==n-1 and arr[index]>=arr[index-1]:
                flag = True
            elif arr[index-1] <= arr[index] and arr[index] >= arr[index+1]:
                flag = True
            else:
                flag = False

        if flag:
            print(1)
        else:
            print(0)
