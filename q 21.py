"""
Given an array a of size N which contains elements from 0 to N-1, you need to find all the elements occurring more than once in the given array. Return the answer in ascending order. If no such element is found, return list containing [-1]. 

Note: The extra space is only for the array to be returned. Try and perform all operations within the provided array. 
"""

class Solution:
    def duplicates(self, arr, n): 
        seen = set()
        duplicates = set()
        
        for num in arr:
            if num in seen:
                duplicates.add(num)
            else:
                seen.add(num)
               
          
        result = sorted(list(duplicates)) if duplicates else [-1]
        return result

if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()