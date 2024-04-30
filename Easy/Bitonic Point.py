"""
Given an array arr of n elements that is first strictly increasing and then maybe strictly decreasing, find the maximum element in the array.
Note: If the array is increasing then just print the last element will be the maximum value.
"""

class Solution:
    def findMaximum(self,arr, n):
        if arr[n-1] > arr[n-2]:
            return arr[n-1]
        l = 0
        h = n - 1
        
        while l <= h:
            m = (l + h) //2
            if arr[m] > arr[m-1] and arr[m] > arr[m+1]:
                return arr[m]
            elif arr[m-1] < arr[m] and arr[m] < arr[m+1]:
                l = m + 1
            else:
                h = m - 1

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaximum(arr, n)
        print(ans)
        tc -= 1
