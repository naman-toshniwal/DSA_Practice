"""
Given an array of integers arr, the length of the array n, and an integer k, find all the unique combinations in arr where the sum of the combination is equal to k. Each number can only be used once in a combination.
"""

class Solution:
    def CombinationSum2(self, arr, n, k):
        ans = []
        arr.sort()
        
        def fun(idx, comb, s):
            if idx == n or s > k:
                if s == k:
                    ans.append(comb)
                return
            
            if s == k:
                ans.append(comb)
                return
            
            for i in range(idx, n):
                if i > idx and arr[i - 1] == arr[i]:
                    continue
                s += arr[i]
                fun(i + 1, comb + [arr[i]], s)
                s -= arr[i]
        
        fun(0, [], 0)
        return ans

for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    ob = Solution()
    result = ob.CombinationSum2(arr, n, k)

    for row in result:
        print(*row)

    if not result:
        print()
