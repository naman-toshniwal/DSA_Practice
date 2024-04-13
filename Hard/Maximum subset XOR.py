"""
Given an array arr[] of N positive integers. Find an integer denoting the maximum XOR subset value in the given array arr[].
"""

class Solution:
    def maxSubsetXOR(self, arr, N):
            if n == 0:
                return 0
            ans = 0
            
            while True:
                m = max(arr)
                if m == 0:
                    return ans
                ans = max(ans, ans^m)
            
                for i in range(n):
                    arr[i] = min(arr[i], arr[i]^m)

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        set=list(map(int,input().split()))
        obj = Solution()
        print(obj.maxSubsetXOR(set,n))
