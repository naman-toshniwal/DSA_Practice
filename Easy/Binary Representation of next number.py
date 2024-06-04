"""
Given a binary representation in the form of a string(s) of a number n, the task is to find a binary representation of n+1.
"""

class Solution:
    def binaryNextNumber(self, s):
        x=int(s,2)
        y=x+1
        res = bin(y)[2:]
        return res

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        S = input()
        ob = Solution()
        ans = ob.binaryNextNumber(S)
        print(ans)
