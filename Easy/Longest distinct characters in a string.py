"""
Given a string S, find the length of the longest substring with all distinct characters. 
"""

class Solution:
    def longestSubstrDistinctChars(self, S):
        length = 0
        seen = set()
        left = 0
        
        for right, char in enumerate(S):
            while char in seen:
                seen.remove(S[left])
                left += 1
            seen.add(char)
            length = max(length, right - left + 1)
        
        return length

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        S = input()
        solObj = Solution()
        ans = solObj.longestSubstrDistinctChars(S)
        print(ans)