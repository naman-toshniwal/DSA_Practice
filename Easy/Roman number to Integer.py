"""
Given a string in roman no format (s)  your task is to convert it to an integer . Various symbols and their values are given below.
I 1
V 5
X 10
L 50
C 100
D 500
M 1000
"""

class Solution:
    def romanToDecimal(self, S): 
        result = 0
        num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i in range(len(S) - 1):
            if num[S[i]] >= num[S[i + 1]]:
                result += num[S[i]]
            else:
                result -= num [S[i]]
            
        result += num[S[-1]]
        return result

if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        ob = Solution()
        S = input()
        print(ob.romanToDecimal(S))