"""
Given an array arr of n integers, count all pairs (arr[i], arr[j]) in it such that i*arr[i] > j*arr[j] and 0 ≤ i < j < n.

Note: 0-based Indexing is followed.
"""

from bisect import bisect_left

class Solution:    
    def countPairs(self, arr, n):
        ordered, count = [], 0
        
        for i in reversed(range(n)):
            ai = arr[i] * i
            j = bisect_left(ordered, ai)
            count += j
            ordered.insert(j, ai)
        return count

def main():
    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob= Solution()
        print(ob.countPairs(a, n))
        T -= 1


if __name__ == "__main__":
    main()
