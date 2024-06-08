"""
You have given two sorted arrays arr1[] & arr2[] of distinct elements. The first array has one element extra added in between. Return the index of the extra element.

Note: 0-based indexing is followed.
"""

class Solution:
    def findExtra(self,n,a,b):
        low, high = 0, len(a) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if mid == len(b):
                break
            elif b[mid] == a[mid]:
                low = mid + 1
            else:
                high = mid - 1
                
        return low

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(Solution().findExtra(n, a, b))
