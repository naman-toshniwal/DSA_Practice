"""
Given a sentence containing several words and numbers. Find the largest number among them which does not contain 9. If no such number exists, return -1.

Note: Numbers and words are separated by spaces only.
"""

class Solution:
    def ExtractNumber(self,s):
        res = [int(i) for i in s.split(" ") if i.isnumeric() and '9' not in i]
        if not res:
            return -1
        return max(res) if '9' not in str(max(res)) else -1

t = int(input())
for _ in range(t):
    S = input()
    ob = Solution()
    ans = ob.ExtractNumber(S)
    print(ans)
