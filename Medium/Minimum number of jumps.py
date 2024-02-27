"""
Given an array of N integers arr[] where each element represents the maximum length of the jump that can be made forward from that element. This means if arr[i] = x, then we can jump any distance y such that y ≤ x.
Find the minimum number of jumps to reach the end of the array (starting from the first element). If an element is 0, then you cannot move through that element.

Note: Return -1 if you can't reach the end of the array.
"""

class Solution:
    def minJumps(self, arr, n):
        reach = count = last = 0
        
        for i in range(len(arr) - 1):
            reach = max(reach, arr[i] + i)
            
            if i == last:
                last = reach
                count += 1
        
        return count if last >= n-1 else -1

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minJumps(Arr,n)
        print(ans)
