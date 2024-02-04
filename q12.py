"""
Given an array of integers and a number K. Find the count of distinct elements in every window of size K in the array.
"""

class Solution:
    def countDistinct(self, nums, n, k):
        hashmap = {}
        
        for i in range(k):
            hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1
            
        l = 0
        res = [len(hashmap)]
        
        for i in range(k, n):
            hashmap[nums[l]] -= 1
            if hashmap[nums[l]] == 0:
                del hashmap[nums[l]]
            l += 1
            
            hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1
            res.append(len(hashmap))
        
        return res

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        res = Solution().countDistinct(arr, n, k)
        for i in res:
            print (i, end = " ")
        print ()