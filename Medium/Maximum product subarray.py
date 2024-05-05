"""
Given an array Arr[] that contains N integers (may be positive, negative or zero). Find the product of the maximum product subarray.
"""

class Solution:
    def maxProduct(self,arr, n):
        negP=arr[0]
        posP=arr[0]
        res=arr[0]
        
        for i in range(1,n):
            temp=max(arr[i],negP*arr[i],posP*arr[i])
            negP=min(arr[i],negP*arr[i],posP*arr[i])
            posP=temp
            res=max(res,posP)
        return res

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr, n)
        print(ans)
        tc -= 1
