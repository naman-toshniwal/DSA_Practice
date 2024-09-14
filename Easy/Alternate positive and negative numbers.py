"""
Given an unsorted array arr containing both positive and negative numbers. Your task is to create an array of alternate positive and negative numbers without changing the relative order of positive and negative numbers.
Note: Array should start with a positive number and 0 (zero) should be considered a positive element.
"""

class Solution:
    def rearrange(self,arr):
        pos = []
        neg = []
        
        for i in range(len(arr)):
            if arr[i] >= 0:
                pos.append(arr[i])
            else:
                neg.append(arr[i])
                
        i = 0
        j = 0
        index = 0

        while i < len(pos) or j < len(neg):
            if i < len(pos):
                arr[index] = pos[i]
                i += 1
                index += 1
            if j < len(neg):
                arr[index] = neg[j]
                j += 1
                index += 1

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.rearrange(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
