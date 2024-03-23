"""
You are given a number N. Find the total count of set bits for all numbers from 1 to N(both inclusive).
"""

class Solution:
    def countSetBits(self,n):
        two = 2
        ans = 0
        N = n
        
        while (n != 0):
            ans += int(N/two) * (two >> 1)
            
            if ((N & (two - 1)) > ((two >> 1) - 1)):
                ans += (N & (two - 1)) - (two >> 1) + 1
            two <<= 1
            n >>= 1
        return ans

if __name__=="__main__":
    for _ in range(int(input())):
        ob=Solution()
        print(ob.countSetBits(int(input())))
