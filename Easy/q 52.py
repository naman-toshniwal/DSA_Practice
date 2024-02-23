"""
Given an infinite supply of each denomination of Indian currency { 1, 2, 5, 10, 20, 50, 100, 200, 500, 2000 } and a target value N. Find the minimum number of coins and/or notes needed to make the change for Rs N. You must return the list containing the value of coins required. 
"""

class Solution:
    def minPartition(self, N):
        currency = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
        change = []
        a = 0
        
        for i in range(len(currency)):
            a = N // currency[i]
            
            if a != 0:
                for j in range(a):
                    change.append(currency[i])
                N = N % currency[i]
        
        return change

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        arr = ob.minPartition(N)
        for i in range(len(arr)):
            print(arr[i],end=" ")
        print()
