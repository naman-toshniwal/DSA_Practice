"""
You are given an array arr[] of size n. Find the total count of sub-arrays having their sum equal to 0.
"""

class Solution:
    def findSubArrays(self,arr,n):
        count = 0 
        sum_dict = {0:1}
        previous_sum = 0
        
        for element in arr:
            previous_sum += element
            
            if previous_sum in sum_dict:
                count += sum_dict[previous_sum]
            
            sum_dict[previous_sum] = sum_dict.get(previous_sum, 0) + 1
        
        return count

if __name__=='__main__':
    t=int(input())
    for tc in range(t):
        
        N=int(input())
        A = [int(x) for x in input().strip().split(' ')]
        ob = Solution()
        print(ob.findSubArrays(A,N))
