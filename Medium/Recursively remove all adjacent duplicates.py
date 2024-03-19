"""
Given a string s, remove all its adjacent duplicate characters recursively. 

Note: For some test cases, the resultant string would be an empty string. In that case, the function should return the empty string only.
"""

class Solution:
    def rremove (self, S):
        res = ""
        i = 0
        
        while i < len(S):
            if i + 1 < len(S) and S[i] == S[i+1]:
                i+=1
                while i < len(S) and S[i] == S[i-1]:
                    i+=1
            else:
                res += S[i]
                i+=1
        
        return res if len(res) == len(S) else self.rremove(res)

if __name__ == '__main__': 
    t = int(input())
    for _ in range (t):
        S = input()
        ob = Solution()
        print(ob.rremove(S))
