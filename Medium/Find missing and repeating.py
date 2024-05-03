"""
Given an unsorted array Arr of size N of positive integers. One number 'A' from set {1, 2,....,N} is missing and one number 'B' occurs twice in array. Find these two numbers.
"""

class Solution:
    def findTwoElement( self,arr, n): 
        ans = [None, None]
    
        for i in range(n):
            idx = abs(arr[i]) - 1
    
            if arr[idx] > 0:
                arr[idx] = -arr[idx]
            else:
                ans[0] = abs(arr[i])
    
        for i in range(n):
            if arr[i] > 0:
                ans[1] = i + 1
                break
    
        return ans
        
        from collections import Counter
        hm = Counter(arr)
        first = [ele for ele, count in hm.items() if count > 1][0]

        for i in range(1, n + 1):
            if i not in hm:
                return first, i

if __name__ == '__main__': 
    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends