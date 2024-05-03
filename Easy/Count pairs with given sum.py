"""
Given an array of N integers, and an integer K, find the number of pairs of elements in the array whose sum is equal to K.
"""

class Solution:
    def getPairsCount(self, arr, n, k):
        f={}
        c=0
        
        for i in arr:
            complement=k-i
            if complement in f:
                c=c+f[complement]
            f[i]=f.get(i,0)+1
        return c

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1
