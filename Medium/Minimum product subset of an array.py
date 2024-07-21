"""
Given an array arr. The task is to find and return the maximum product possible with the subset of elements present in the array.

Note:

The maximum product can be a single element also.
Since the product can be large, return it modulo 109 + 7.
"""

class Solution:
    def findMaxProduct(self, arr):
        ans, maxneg, mod = 1, float('-inf'), 10**9+7
        
        for i in arr:
            if i != 0:
                ans *= i
            if i < 0 and maxneg < i:
                maxneg = i
                
        if ans < 0:
            ans //= maxneg
        ans = ans%mod
        return ans

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        arr = list(map(int, data[index:index + n]))
        index += n
        solution = Solution()
        ans = solution.findMaxProduct(arr)
        results.append(ans)
    
    for result in results:
        print(result)
