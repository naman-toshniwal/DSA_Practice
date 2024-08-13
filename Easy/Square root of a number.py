"""
Given an integer n, find the square root of n. If n is not a perfect square, then return the floor value.

Floor value of any number is the greatest Integer which is less than or equal to that number
"""

from math import sqrt

class Solution:
    def floorSqrt(self, n): 
        res = sqrt(n)
        return int(res)

def main():
    T = int(input())
    while (T > 0):
        x = int(input())
        print(Solution().floorSqrt(x))
        T -= 1

if __name__ == "__main__":
    main()
