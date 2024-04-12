"""
Given an array of integers of size N find minimum xor of any 2 elements.
"""

class Solution:
    def minxorpair (self, N, arr):
        ans=999999999
        arr=sorted(arr)

        for i in range(N-1):
            ans=min(arr[i]^arr[i+1],ans)
        return ans

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
    
        ob = Solution()
        print(ob.minxorpair(N,arr))
