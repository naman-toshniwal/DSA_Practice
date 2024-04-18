"""
You are given an integer n and an integer array arr of size n+2. All elements of the array are in the range from 1 to n. Also, all elements occur once except two numbers which occur twice. Find the two repeating numbers.
Note: Return the numbers in their order of appearing twice. So, if X and Y are the repeating numbers, and X's second appearance comes before second appearance of Y, then the order should be (X, Y).
"""

class Solution:
    def twoRepeated(self, arr , n):
        count = {}
        rep = []
        
        for i in arr:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
            
            if (count[i] == 2):
                rep.append(i)
        
        return rep

import math
def main():
        T=int(input())
        while(T>0):
            N=int(input())
            A=[int(x) for x in input().strip().split()]
            obj = Solution()
            ans = obj.twoRepeated(A,N)
            print(ans[0], ans[1])
            T-=1

if __name__ == "__main__":
    main()
