"""
You are given an integer array arr[] of size n, representing n number of people in a party, each person is denoted by an integer. Couples are represented by the same number ie: two people have the same integer value, it means they are a couple. Find out the only single person in the party of couples.

NOTE: It is guarantee that there exist only one single person in the party.
"""

from collections import Counter

class Solution:
    def findSingle(self, n, arr):
        count=Counter(arr)
        counted=dict(count)
        for i in counted:
            if counted[i]%2!=0:
                return i

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        
        ob = Solution()
        print(ob.findSingle(N, arr))
