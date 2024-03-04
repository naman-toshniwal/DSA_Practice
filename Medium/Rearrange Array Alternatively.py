"""
Given a sorted array of positive integers. Your task is to rearrange the array elements alternatively i.e first element should be max value, second should be min value, third should be second max, fourth should be second min and so on.
Note: Modify the original array itself. Do it without using any extra space. You do not have to return anything.
"""

class Solution:
    def rearrange(self,arr, n): 
        l = 0
        h = n - 1
        max_item = arr[h] + 1
        
        for i in range(n):
            if i % 2 == 0:
                arr[i] += (arr[h] % max_item) * max_item
                h -= 1
            else:
                arr[i] += (arr[l] % max_item) * max_item
                l += 1
                
        for i in range(n):
            arr[i] //= max_item

import math
def main():
        T=int(input())
        while(T>0):           
            n=int(input())           
            arr=[int(x) for x in input().strip().split()]          
            ob=Solution()
            ob.rearrange(arr,n)
            
            for i in arr:
                print(i,end=" ")        
            print()           
            T-=1

if __name__ == "__main__":
    main()
