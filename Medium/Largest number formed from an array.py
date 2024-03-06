"""
Given an array of strings arr[] of length n representing non-negative integers, arrange them in a manner, such that, after concatanating them in order, it results in the largest possible number. Since the result may be very large, return it as a string.
"""

class Solution:

    def printLargest(self, n, arr):
        A = sorted(arr, key=lambda x: str(x)*10, reverse = True)
        return ''.join([str(i) for i in A])

import functools
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(str, input().strip().split()))
        ob = Solution()
        ans = ob.printLargest(n, arr)
        print(ans)
        tc -= 1
