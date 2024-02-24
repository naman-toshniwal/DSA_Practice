"""
Given an array arr[ ] of length N consisting cost of N toys and an integer K depicting the amount with you. Your task is to find maximum number of toys you can buy with K amount. 
"""

class Solution:
    def toyCount(self, N, K, arr):
        arr.sort()
        count = 0
        
        for i in range(N):
            if K >= arr[i]:
                K -= arr[i]
                count += 1
        
        return count

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, K = [int(x) for x in input().split()]
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])
        
        ob = Solution()
        print(ob.toyCount(N, K, arr))