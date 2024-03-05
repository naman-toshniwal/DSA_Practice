"""
Given an array of n distinct elements. Find the minimum number of swaps required to sort the array in strictly increasing order.
"""

class Solution:
    def minSwaps(self, nums):
        v = [(nums[i], i) for i in range(len(nums))]
        v = sorted(v)
        count = 0
        i = 0
        
        while i < len(nums):
            num, index = v[i]
            
            if i != index:
                count += 1
                v[i], v[index] = v[index], v[i]
                i -= 1
            i += 1
        return count

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        nums = list(map(int, input().split()))
        obj = Solution()
        ans = obj.minSwaps(nums)
        print(ans)
