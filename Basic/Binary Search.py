"""
Given a sorted array of size N and an integer K, find the position(0-based indexing) at which K is present in the array using binary search.
"""

class Solution:    
    def binarysearch(self, arr, n, k):
        for i in range(len(arr)):
            if k == arr[i]:
                return i
        
        return -1

if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int, input().strip().split(' ')))
        k=int(input())
        ob = Solution()
        print (ob.binarysearch(arr, n, k))
