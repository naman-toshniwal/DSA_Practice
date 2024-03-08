"""
Given a collection of Intervals, the task is to merge all of the overlapping Intervals.
"""

class Solution:
    def overlappedInterval(self, Intervals):
        ans = []
        Intervals = sorted(Intervals)
        
        for interval in Intervals:
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])
        
        return ans

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        a = list(map(int, input().strip().split()))
        Intervals = []
        j = 0
        for i in range(n):
            x = a[j]
            j += 1
            y = a[j]
            j += 1
            Intervals.append([x,y])
        obj = Solution()
        ans = obj.overlappedInterval(Intervals)
        for i in ans:
            for j in i:
                print(j, end = " ")
        print()
