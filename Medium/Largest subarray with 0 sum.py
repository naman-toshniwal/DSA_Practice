"""
Given an array having both positive and negative integers. The task is to compute the length of the largest subarray with sum 0.
"""

class Solution:
    def maxLen(self, n, arr):
        presum = 0
        dict = {}
        max_length = 0
        
        for i in range(len(arr)):
            presum += arr[i]
            if presum == 0:
                max_length = i + 1
            
            if presum in dict:
                max_length = max(max_length, i - dict[presum])
            else:
                dict[presum] = i
        
        return max_length

if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
