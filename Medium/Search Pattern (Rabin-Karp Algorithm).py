"""
Given two strings, one is a text string and other is a pattern string. The task is to print the indexes of all the occurences of pattern string in the text string. For printing, Starting Index of a string should be taken as 1. The strings will only contain lowercase English alphabets ('a' to 'z').
"""

class Solution:
    def search(self, pattern, text):
        result = []
        n = len(pattern)
        
        for i in range(len(text)):
            if (text[i:i+n] == pattern):
                result.append(i + 1)
        
        return result

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        for value in ans:
            print(value,end = ' ')
        print()
