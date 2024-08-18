"""
Given an array of integers arr, return true if it is possible to split it in two subarrays (without reordering the elements), such that the sum of the two subarrays are equal. If it is not possible then return false.
"""

class Solution:
    def canSplit(self, nums):
        left, right = 0, len(nums) - 1
        current_sum = 0

        # Traverse the array from both ends towards the middle
        while left <= right:
            # If current_sum is non-positive, add the left element and move left pointer
            if current_sum <= 0:
                current_sum += nums[left]
                left += 1
            # If current_sum is positive, subtract the right element and move right pointer
            else:
                current_sum -= nums[right]
                right -= 1

        # Check if current_sum is zero, indicating a possible split
        return current_sum == 0

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    t = int(data[0])
    index = 1
    for _ in range(t):
        arr = list(map(int, data[index].split()))
        index += 1

        obj = Solution()
        res = obj.canSplit(arr)
        if (res):
            print("true")
        else:
            print("false")
