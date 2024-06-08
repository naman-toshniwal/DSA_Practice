"""
Given n integer ranges, the task is to return the maximum occurring integer in the given ranges. If more than one such integer exists, return the smallest one.
The ranges are in two arrays l[] and r[].  l[i] consists of the starting point of the range and r[i] consists of the corresponding endpoint of the range & a maxx which is the maximum value of r[].

For example, consider the following ranges.
l[] = {2, 1, 3}, r[] = {5, 3, 9)
Ranges represented by the above arrays are.
[2, 5] = {2, 3, 4, 5}
[1, 3] = {1, 2, 3}
[3, 9] = {3, 4, 5, 6, 7, 8, 9}
The maximum occurred integer in these ranges is 3.
"""

class Solution:
    def maxOccured(self,n, l, r, maxx):
        arr = [0] * (maxx + 2)
        
        for i in range(n):
            arr[l[i]] += 1
            if r[i] + 1 <= maxx:
                arr[r[i] + 1] -= 1
        
        max_occur = 0
        max_value = 0
        current_sum = 0
        
        for i in range(maxx + 1):
            current_sum += arr[i]
            if current_sum > max_value:
                max_value = current_sum
                max_occur = i
        
        return max_occur

import math
A = [0] * 1000000

def main():
    T = int(input())
    while (T > 0):
        global A
        A = [0] * 1000000
        n = int(input())
        l = [int(x) for x in input().strip().split()]
        r = [int(x) for x in input().strip().split()]
        maxx = max(r)
        ob = Solution()
        print(ob.maxOccured(n, l, r, maxx))
        T -= 1
if __name__ == "__main__":
    main()
