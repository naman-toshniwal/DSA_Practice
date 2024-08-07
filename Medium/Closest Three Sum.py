"""
Given an array, arr of integers, and another number target, find three integers in the array such that their sum is closest to the target. Return the sum of the three integers.

Note: If there are multiple solutions, return the maximum one.
"""

class Solution:
    def threeSumClosest(self, arr, target):
        n = len(arr)
        arr.sort()
        diff = float('inf')
        ans = None
        
        for i in range(n):
            first = arr[i]
            start = i + 1
            end = n - 1

            while start < end:
                current_sum = first + arr[start] + arr[end]
                if current_sum == target:
                    return target
                current_diff = abs(current_sum - target)

                if current_diff < diff or (current_diff == diff and current_sum > ans):
                    diff = current_diff
                    ans = current_sum

                if current_sum > target:
                    end -= 1
                else:
                    start += 1

        return ans

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        A = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.threeSumClosest(A, k))
