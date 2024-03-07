"""
Given 2 sorted arrays Ar1 and Ar2 of size N each. Merge the given arrays and find the sum of the two middle elements of the merged array.
"""

class Solution:
    def findMidSum(self, ar1, ar2, n): 
        ar1.extend(ar2)
        ar1 = sorted(ar1)
        sum = ar1[n-1] + ar1[n]
        return sum

if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        ar1=list(map(int, input().strip().split()))
        ar2=list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMidSum(ar1, ar2, n)
        print(ans)
        tc=tc-1
