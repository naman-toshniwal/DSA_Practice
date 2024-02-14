"""
In a party of N people, each person is denoted by an integer. Couples are represented by the same number. Find out the only single person in the party of couples.
"""

class Solution:
    def findSingle(self, N, arr):
        for i in range(N):
            if (arr.count(arr[i]) == 1):
                return arr[i]

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        
        ob = Solution()
        print(ob.findSingle(N, arr))
