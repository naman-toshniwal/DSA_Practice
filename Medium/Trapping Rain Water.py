"""
Given an array arr[] of N non-negative integers representing the height of blocks. If width of each block is 1, compute how much water can be trapped between the blocks during the rainy season. 
"""

class Solution:
    def trappingWater(self, arr,n):
        if n <= 2:
            return 0
        
        left, right = 0, n-1
        left_max = right_max = water_trapped = 0
        
        while (left < right):
            if (arr[left] < arr[right]):
                if arr[left] >= left_max:
                    left_max = arr[left]
                else:
                    water_trapped += left_max - arr[left]
                left += 1
            else:
                if arr[right] >= right_max:
                    right_max = arr[right]
                else:
                    water_trapped += right_max - arr[right]
                right -= 1
        
        return water_trapped

import math
def main():
        T=int(input())
        while(T>0):
            n=int(input())
            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))            
            T-=1

if __name__ == "__main__":
    main()
