"""
Given an array Arr of size N, print the second largest distinct element from an array. If the second largest element doesn't exist then return -1.
"""

class Solution:
    def print2largest(self, arr, n):
        arr.sort(reverse = True)
        
        for i in range(1, len(arr)):
            if arr[i] != arr[0]:
                return arr[i]
                
        return -1

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1
