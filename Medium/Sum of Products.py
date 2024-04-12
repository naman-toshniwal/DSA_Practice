"""
Given an array arr[] of size n. Calculate the sum of Bitwise ANDs ie: calculate sum of arr[i] & arr[j] for all the pairs in the given array arr[] where i < j.
"""

class Solution:
    def pairAndSum(self, n, arr):
        total_sum = 0

        for bit in range(32):
            count = 0
            
            for num in arr:
                if num & (1 << bit):
                    count += 1

            total_sum += count * (count - 1) // 2 * (1 << bit)
        return total_sum

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        Arr=list(map(int,input().strip().split(' ')))
        ob=Solution()
        print(ob.pairAndSum(N,Arr))
