"""
Given an array of integers nums and a number k, write a function that returns true if given array can be divided into pairs such that sum of every pair is divisible by k.
"""

from collections import Counter as K

class Solution:
    def canPair(self, nuns, k):
        q = K([i%k for i in nuns])
        status = True
        
        for i in range(k):
            a = q.get(i, 0)
            b = q.get((k-i)%k, 0)
            
            if a != b:
                return False
            
            if i == (k-i)%k and a%2 != 0:
                return False
        return True

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n, k = input().split()
        n = int(n)
        k = int(k)
        nums = list(map(int, input().split()))
        ob = Solution()
        ans = ob.canPair(nums, k)
        if(ans):
            print("True")
        else:
            print("False")
