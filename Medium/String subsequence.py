"""
Given two strings, s1 and s2, count the number of subsequences of string s1 equal to string s2.

Return the total count modulo 1e9+7.
"""

from functools import lru_cache

class Solution:
    def countWays(self, s1 : str, s2 : str) -> int:
        n,m,MOD=len(s1),len(s2),1000000007
        pre=[0]*(m+1)
        pre[m]=1
        
        for i in range(n-1,-1,-1):
            curr=[0]*(m+1)
            curr[m]=1
            
            for j in range(m-1,-1,-1):
                ans=pre[j]%MOD
                if s1[i]==s2[j]:
                    ans+=pre[j+1]%MOD
                curr[j]=ans%MOD
            pre=[k for k in curr]
        return curr[0]%MOD

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s1 = (input())
        s2 = (input())
        obj = Solution()
        res = obj.countWays(s1, s2)
        print(res)
