"""
Given a number x, reverse its binary form and return the answer in decimal.
"""

class Solution:
    def reversedBits(self, x):
        res = 0
        for i in range(32):
            bit = 1 & (x >> i)
            res = res | (bit << (31-i))
        return res

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        X=int(input())
        
        ob = Solution()
        print(ob.reversedBits(X))
