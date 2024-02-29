"""
Given an array of integers. Find the Inversion Count in the array. 

Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted. If the array is already sorted then the inversion count is 0.
If an array is sorted in the reverse order then the inversion count is the maximum. 
Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.
"""

class Solution:
    def merge(self, left, right):
        i = j = count = 0
        merged = []
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                count += len(left) - i
        
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, count
        
    def mergeSortAndCount(self, A):
        if len(A) <= 1:
            return A, 0
        
        middle = len(A) // 2
        left, left_count = self.mergeSortAndCount(A[:middle])
        right, right_count = self.mergeSortAndCount(A[middle:])
        merged, merge_count = self.merge(left, right)
        return merged, left_count + right_count + merge_count
        
    def inversionCount(self, arr, n):
        _, count = self.mergeSortAndCount(arr)
        return count

import atexit
import io
import sys
_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER
@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a,n))
