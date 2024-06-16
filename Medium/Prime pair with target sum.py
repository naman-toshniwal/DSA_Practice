"""
Given a number n, find out if n can be expressed as a+b, where both a and b are prime numbers. If such a pair exists, return the values of a and b, otherwise return [-1,-1] as an array of size 2.
Note: If [a, b] is one solution with a <= b, and [c, d] is another solution with c <= d, and a < c then  [a, b] is considered as our answer.
"""

from typing import List

class Solution:
    def getPrimes(self, n : int) -> List[int]:
        arr = self.primeNumbers(n)
        if arr[0] == n:
            return [-1,-1]
        else:
            return arr

    def primeNumbers(self,n):
        if n<=1:
            return False
        isprime = [True]*(n+1)
        
        i = 2
        k = n
        while i<=n:
            if isprime[i]:
                for j in range(i*i,n+1,i):
                    isprime[j]=False
            i+=1
        arr = [k,k]
        
        for i in range(2,k+1):
            if isprime[i] and isprime[k-i] and i<=arr[0]:
                arr[0] = i
                arr[1] = k-i
                return arr
        return arr

class IntArray:
    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        obj = Solution()
        res = obj.getPrimes(n)
        IntArray().Print(res)
