"""
Given a positive integer n. Your task is to generate a string list of all n-bit binary numbers where, for any prefix of the number, there are more or an equal number of 1's than 0's. The numbers should be sorted in decreasing order of magnitude.
"""

class Solution:
    def NBitBinary(self, n):
        import sys
        sys.setrecursionlimit(10**6)
        ans = []
        
        def dfs(s, k):
            m = len(s)
            
            if m == n:
                ans.append(s)
                return 
            
            if k*2  > m:
                dfs(s+"0", k)
            dfs(s+"1",k+1)
        
        dfs("",0)
        return sorted(ans,reverse=True)

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        ob = Solution()	
        answer = ob.NBitBinary(n)
        for value in answer:
            print(value,end=" ")
        print()
