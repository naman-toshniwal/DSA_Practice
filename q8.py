"""
Given a sorted array arr[] of size N. Find the element that appears only once in the array. All other elements appear exactly twice. 
"""

class Solution:
    def findOnce(self,arr : list, n : int):
        arr_sum = sum(arr)
        set_sum = sum(set(arr))
        num = (set_sum * 2) - arr_sum
        return num

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.findOnce(arr, n))
