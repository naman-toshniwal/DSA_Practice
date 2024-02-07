"""
Given a String S, reverse the string without reversing its individual words. Words are separated by dots.
"""


class Solution:
    def reverseWords(self,S):
        words = S.split('.')
        rev_words = words[::-1]
        rev_string = '.'.join(rev_words)
        return rev_string

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        print(obj.reverseWords(s))
