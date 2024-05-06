"""
You are given a string s. You need to reverse the string.
"""

class Solution:
     def reverseWord(self, str: str) -> str:
        return str[::-1]

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        s = input()
        ob = Solution()
        print(ob.reverseWord(s))
        t = t-1
