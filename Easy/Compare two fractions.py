"""
You are given a string str containing two fractions a/b and c/d, compare them and return the greater. If they are equal, then return "equal".

Note: The string str contains "a/b, c/d"(fractions are separated by comma(,) & space( )). 
"""

class Solution:
    def compareFrac (self, str):
        f1,f2=str.split(', ')
        v1,v2=eval(f1),eval(f2)

        if v1==v2:
            return 'equal'
        elif v1<v2:
            return f2
        else:
            return f1

import re
if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        str = input()
        print(ob.compareFrac(str))
