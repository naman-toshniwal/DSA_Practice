"""
Given an array nums[], construct a Product Array nums[] such that nums[i] is equal to the product of all the elements of nums except nums[i].
"""

class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        ans = [1] * n
        
        # Step 1: Calculate prefix products
        left = 1
        for i in range(n):
            ans[i] = left
            left *= nums[i]
        
        # Step 2: Calculate suffix products and finalize the result
        right = 1
        for i in range(n-1, -1, -1):
            ans[i] *= right
            right *= nums[i]
        
        return ans

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]
        ans = Solution().productExceptSelf(arr)
        print(*ans)
