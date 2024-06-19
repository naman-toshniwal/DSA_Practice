"""
You are given a perimeter & the area. Your task is to return the maximum volume that can be made in the form of a cuboid from the given perimeter and surface area.
Note: Round off to 2 decimal places and for the given parameters, it is guaranteed that an answer always exists.
"""

class Solution:
    def maxVolume(self, p, a):
        x = (p - math.sqrt(p**2 - 24*a)) / 12
        V = (p*x**2 - 8*x**3)/4
        return round(V, 2)

import math
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        perimeter, area = [int(x) for x in input().split()]
        ob = Solution()
        print('%.2f' % ob.maxVolume(perimeter, area))
