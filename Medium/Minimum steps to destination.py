"""
Given an infinite number line. You start at 0 and can go either to the left or to the right. The condition is that in the ith move, you must take i steps. Given a destination d, find the minimum number of steps required to reach that destination.
"""

class Solution:
    def minSteps(self, d):
        for i in range(1,2* d):
            if (((i*(i+1))//2) + d)%2 == 0 and ((i*(i+1))//2) >= d:
                return i

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        d = int(input())
        ob = Solution()
        print(ob.minSteps(d))
