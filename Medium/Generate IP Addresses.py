"""
Given a string S containing only digits, Your task is to complete the function genIp() which returns a vector containing all possible combinations of valid IPv4 IP addresses and takes only a string S as its only argument.
Note: Order doesn't matter. A valid IP address must be in the form of A.B.C.D, where A, B, C, and D are numbers from 0-255. The numbers cannot be 0 prefixed unless they are 0.
"""

class Solution:
    def genIp(self, s):
        result = []
        
        if len(s) > 12 or len(s) < 4:
            return result
        
        def backtrack(i, currIp, dots):
            if dots == 4 and i == len(s):
                result.append(currIp[:-1])
                return
            
            if dots > 4:
                return
            
            for j in range(i, min(i+3, len(s))):
                if int(s[i:j+1]) < 256 and (i ==j or s[i] != "0"):
                    backtrack(j+1, currIp + s[i:j+1] + '.', dots+1)
        
        backtrack(0, "", 0)
        return result

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s = input().strip()
        res = Solution().genIp(s)
        res.sort()
        if(len(res)):
            for u in res:
                print(u)
        else:
            print(-1)
