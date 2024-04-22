"""
Given an array arr of size n containing non-negative integers, the task is to divide it into two sets S1 and S2 such that the absolute difference between their sums is minimum and find the minimum difference
"""

class Solution:
    def minDifference(self, arr, n):
        total = sum(arr)
        memo = [False] * (total + 1)
        
        for step in range(len(arr)):
            val = arr[step]
            for i in range(len(memo) - 1, -1, -1):
                if memo[i]:
                    memo[i + val] = True
            memo[val] = True
        res = float('inf')
        
        for i in range(len(memo)):
            if memo[i]:
                diff = abs((total - i) - i)
                res = min(res, diff)

        return res

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minDifference(arr, N)
        print(ans)
