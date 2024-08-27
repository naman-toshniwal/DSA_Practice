"""
Given two strings pattern and str which may be of different size, You have to return 1 if the wildcard pattern i.e. pattern, matches with str else return 0. All characters of the string str and pattern always belong to the Alphanumeric characters.

The wildcard pattern can include the characters ? and *
'?' - matches any single character.
'*' - Matches any sequence of characters (including the empty sequence).

Note: The matching should cover the entire str (not partial str).
"""

import re

class Solution:
    def wildCard(self, pattern, string):
        p = "^" + re.sub("\*+", "[a-z]*", pattern).replace("?", "[a-z]") + "$"
        return 1 if re.search(p, string) else 0

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        pattern = input().strip()
        string = input().strip()
        if Solution().wildCard(pattern, string):
            print(1)
        else:
            print(0)
