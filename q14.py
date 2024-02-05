"""
Given a string S. The task is to find the first repeated character in it. We need to find the character that occurs more than once and whose index of second occurrence is smallest. S contains only lowercase letters.
"""

class Solution:

    def firstRepChar(self, s):
        list = []
        
        for i in s:
            if i not in list:
                list.append(i)
            else:
                return i
        return -1

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        print(solObj.firstRepChar(s))