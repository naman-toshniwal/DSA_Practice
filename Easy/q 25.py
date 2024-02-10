"""
Given a string without spaces, the task is to remove duplicates from it.

Note: The original order of characters must be kept the same. 
"""

class Solution:
    def removeDups(self, S):
        str = ''
        
        for char in S:
            if char not in str:
                str += char
        
        return str

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        s = input()
        
        ob = Solution()	
        answer = ob.removeDups(s)
        
        print(answer)