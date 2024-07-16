"""
Given a string s without spaces, a character ch and an integer count. Your task is to return the substring that remains after the character ch has appeared count number of times.
Note:  Assume upper case and lower case alphabets are different. “”(Empty string) should be returned if it is not possible, or the remaining substring is empty.
"""

class Solution:
    def printString(self, s, ch, count):
        cnt = 0
        for i in range(len(s)):
            if s[i] == ch:
                cnt += 1
                if cnt == count:
                    return s[i+1:]
        
        return ""

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()
        ch = input()[0]
        count = int(input())
        ob = Solution()
        answer = ob.printString(s, ch, count)
        print(answer)
