"""
You have N books, each with A[i] number of pages. M students need to be allocated contiguous books, with each student getting at least one book.
Out of all the permutations, the goal is to find the permutation where the sum of maximum number of pages in a book allotted to a student should be minimum, out of all possible permutations.

Note: Return -1 if a valid assignment is not possible, and allotment should be in contiguous order (see the explanation for better understanding).
"""

class Solution:
    def findPages(self,A, N, M):
        start = max(A)
        end = sum(A)
        
        if (N < M):
            return -1
        
        while (start <= end):
            mid = (start + end) // 2
            c = 0
            a = 1
            
            for i in range(len(A)):
                if (c + A[i]) > mid:
                    a += 1
                    c = A[i]
                else:
                    c += A[i]
                
            if (a > M):
                start  = mid + 1
            else:
                end = mid - 1
            a = 1
            
        return start    

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        m=int(input())
        
        ob=Solution()
        
        print(ob.findPages(arr,n,m))
