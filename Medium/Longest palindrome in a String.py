"""
Given a string S, find the longest palindromic substring in S. Substring of string S: S[ i . . . . j ] where 0 ≤ i ≤ j < len(S). Palindrome string: A string that reads the same backward. More formally, S is a palindrome if reverse(S) = S. In case of conflict, return the substring which occurs first ( with the least starting index).
"""

class Solution:
    def longestPalin(self, S):
        result = ""
        s2 = 0
        
        if (S == S[::-1]):
            return (S)
            
        for i in range(len(S)):
            st = ''
            s1 = 0
            
            for j in range(i, len(S)):
                st += S[j]
                s1 += 1
                
                if (st == st[::-1]):
                    if (s1 > s2):
                        result = st
                        s2 = s1
        
        return result

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        S = input()
        ob = Solution()
        ans = ob.longestPalin(S)
        print(ans)
