"""
We have a horizontal number line. On that number line, we have gas stations at positions stations[0], stations[1], ..., stations[N-1], where n = size of the stations array. Now, we add k more gas stations so that d, the maximum distance between adjacent gas stations, is minimized. We have to find the smallest possible value of d. Find the answer exactly to 2 decimal places.
"""

class Solution:
    def findSmallestMaxDist(self, stations, K):
        def is_feasible(d):
            count = 0
            for i in range(1, len(stations)):
                count += (stations[i] - stations[i - 1]) // d
            return count <= K
            
        low, high = 0, stations[-1] - stations[0]
        while high - low > 1e-6:
            mid = (low + high) / 2
            
            if is_feasible(mid):
                high = mid
            else:
                low = mid
                
        return round(high, 2)

import math
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        stations = list(map(int, input().split()))
        K = int(input())
        ob = Solution()
        print('%.2f' % ob.findSmallestMaxDist(stations, K))
