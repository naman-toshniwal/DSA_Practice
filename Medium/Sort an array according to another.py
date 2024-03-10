"""
Given two integer arrays A1[ ] and A2[ ] of size N and M respectively. Sort the first array A1[ ] such that all the relative positions of the elements in the first array are the same as the elements in the second array A2[ ].
See example for better understanding.
Note: If elements are repeated in the second array, consider their first occurance only.
"""

from collections import Counter
class Solution:
    def relativeSort (self,A1, N, A2, M):
        mp = Counter(A1)
        ans = []
        for i in A2:
            if mp[i]:
                fq = mp[i]
                ans += [i]*fq
                del mp[i]
        
        if mp:
            for i in sorted(mp.keys()):
                fq = mp[i]
                ans += [i]* fq
            return ans
        return ans

if __name__ == '__main__':
    t = int (input ())
    while t > 0:
        n, m = list(map(int, input().split()))
        a1 = list(map(int, input().split()))
        a2 = list(map(int, input().split()))
        ob=Solution()
        a1 = ob.relativeSort (a1, n, a2, m)
        print (*a1, end = " ")
        print ()        
        t -= 1
