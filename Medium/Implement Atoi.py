"""
Given a string, s, the objective is to convert it into integer format without utilizing any built-in functions. If the conversion is not feasible, the function should return -1.

Note: Conversion is feasible only if all characters in the string are numeric or if its first character is '-' and rest are numeric.
"""

class Solution:
    def atoi(self,s):
        s = s.split("-")
        
        if len(s) == 1:
            if s[0].isdigit():
                return int(s[0])
            else:
                return -1
        else:
            if s[1].isdigit():
                return -int(s[1])
            else:
                return -1

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        string = input().strip();
        ob=Solution()
        print(ob.atoi(string))
