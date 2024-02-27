"""
Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.
"""

class Solution:
    def sort012(self,arr,n):
        l = m = 0
        h = n - 1
        
        while m <= h:
            if arr[m] == 0:
                arr[l], arr[m] = arr[m], arr[l]
                l += 1
                m += 1
            
            elif arr[m] == 1:
                m += 1
            
            else:
                arr[h], arr[m] = arr[m], arr[h]
                h -= 1
        
        return arr

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()
