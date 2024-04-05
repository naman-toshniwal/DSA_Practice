"""
Given an array nums of n positive integers. Find the minimum number of operations required to modify the array such that array elements are in strictly increasing order (nums[i] < nums[i+1]).
Changing a number to greater or lesser than original number is counted as one operation.

Note: Array elements can become negative after applying operation.
"""

class Solution:
    def min_operations(self, nums):
        n = len(nums)
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[i] - nums[j] >= i - j:
                    dp[i] = max(dp[i], dp[j] + 1)

        max_ops = max(dp)
        return n - max_ops

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        nums = list(map(int, input().split()))
        ob = Solution();
        ans = ob.min_operations(nums)
        print(ans)
