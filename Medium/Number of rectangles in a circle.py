"""
Given a circular sheet of radius, r. Find the total number of rectangles with integral length and width that can be cut from the sheet that can fit on the circle, one at a time.
"""

class Solution:
    def rectanglesInCircle(self, r):
        diameter = 2 * r
        rectangle_count = 0
        square_diameter = diameter * diameter
        
        for l in range(1, diameter):
            for b in range(1, diameter):
                diagonal = l * l + b * b
                if diagonal <= square_diameter:
                    rectangle_count += 1
        
        return rectangle_count

import math
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.rectanglesInCircle(N)
        print(ans)
