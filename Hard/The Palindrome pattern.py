"""
Given a two-dimensional integer array arr of dimensions n x n, consisting solely of zeros and ones, identify the row or column (using 0-based indexing) where all elements form a palindrome. If multiple palindromes are identified, prioritize the palindromes found in rows over those in columns. Within rows or columns, the palindrome with the smaller index takes precedence. The result should be represented by the index followed by either 'R' or 'C', indicating whether the palindrome was located in a row or column. The output should be space-separated. If no palindrome is found, return the string -1.
"""

class Solution:
    def pattern (self, arr):
        def is_palin(nums):
            for i in range(len(nums)//2):
                if nums[i] != nums[-i-1]:
                    return False
            return True
        
        n = len(arr)
        for i in range(n):
            if is_palin(arr[i]):
                return "{} R".format(i)
        
        for i in range(n):
            tmp = []
            for j in range(n):
                tmp.append(arr[j][i])
            if is_palin(tmp):
                return "{} C".format(i)
                
        return -1

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        a = list()
        c = 0
        for i in range(0, n):
            X = list()
            for j in range(0, n):
                X.append(arr[c])
                c += 1
            a.append(X)
        ans = ob.pattern(a)
        print(ans)
