"""
Given an array arr[] denoting heights of N towers and a positive integer K.

For each tower, you must perform exactly one of the following operations exactly once.

Increase the height of the tower by K
Decrease the height of the tower by K
Find out the minimum possible difference between the height of the shortest and tallest towers after you have modified each tower.

You can find a slight modification of the problem here.
Note: It is compulsory to increase or decrease the height by K for each tower. After the operation, the resultant array should not contain any negative integers.
"""

class Solution:
    def getMinDiff(self, arr, n, k):
        arr = sorted(arr)
        result = arr[n-1] - arr[0]
        smallest = arr[0] + k
        largest = arr[n-1] - k
        
        for i in range(n-1):
            minimum = min(smallest, arr[i+1] - k)
            maximum = max(largest, arr[i] + k)
            
            if minimum < 0:
                continue
            result = min(result, maximum - minimum)
        return result

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, n, k)
        print(ans)
        tc -= 1
