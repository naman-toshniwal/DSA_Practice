"""
Given an array of N strings, find the longest common prefix among all strings present in the array.
"""

class Solution:
    def longestCommonPrefix(self, arr, n):
        s = arr[0]
        
        for i in range(n):
            if len(s) > len(arr[i]):
                s = arr[i]
            
        for i in range(n):
            for j in range(len(s)):
                if s[j] != arr[i][j]:
                    s = s[:j]
                    break
        
        if s == "":
            return -1
        else:
            return s

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        arr = [x for x in input().strip().split(" ")]
        
        ob=Solution()
        print(ob.longestCommonPrefix(arr, n))