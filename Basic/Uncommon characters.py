"""
Given two strings A and B consisting of lowercase english characters. Find the characters that are not common in the two strings. 

Note :- Return the string in sorted order.
"""

class Solution:
    def UncommonChars(self,A, B):
        ans=''
        
        for i in A:
            if i not in B:
                ans+=i
        
        for i in B:
            if i not in A:
                ans+=i
        
        if not ans:
            return -1
        else:
            return ''.join(sorted(set(ans)))

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        A = input()
        B = input()
        ob = Solution()
        print(ob.UncommonChars(A, B))
