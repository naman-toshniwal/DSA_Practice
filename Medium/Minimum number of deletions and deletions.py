"""
Given two strings str1 and str2. The task is to remove or insert the minimum number of characters from/in str1 so as to transform it into str2. It could be possible that the same character needs to be removed/deleted from one point of str1 and inserted to some another point.
"""

class Solution:
    def minOperations(self, s1, s2):
        dp = [[0 for _ in range(len(s2))] for _ in range(len(s1))]
        
        for i in range(len(s1)):
            for j in range(len(s2)):
                dp[i][j] = max(dp[i][j - 1] if j - 1 >= 0 else 0, dp[i-1][j] if i - 1 >= 0 else 0)
                if s1[i] == s2[j]:
                    dp[i][j] = (dp[i - 1][j - 1] if i - 1 >= 0 and j - 1 >= 0 else 0) + 1
        
        return len(s1) + len(s2) - 2 * dp[-1][-1]

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        s1,s2 = input().split()
        ob = Solution()
        ans = ob.minOperations(s1,s2)
        print(ans)
