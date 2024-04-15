"""
Given two arrays a and b both of size n. Given q queries in an arrray query each having a positive integer x denoting an index of the array a. For each query, your task is to find all the elements less than or equal to a[x] in the array b.
"""

class Solution:
    def countElements(self, a, b, n, query, q):
        size = max(max(a),max(b))
        memo = [0] * (size+1)
        ans = []
        
        for i in range(n):
            memo[b[i]] +=1
        
        for i in range(1,size+1):
            memo[i] += memo[i-1]
        
        for i in range(q):
            ans.append(memo[a[query[i]]])
        return ans

t = int(input())
for _ in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    q = int(input())
    query = []
    ob = Solution()
    for i in range(q):
        query.append(int(input()))
    ans = ob.countElements(a, b, n, query, q)
    for i in range(q):
        print(ans[i])
