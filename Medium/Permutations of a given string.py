"""
Given a string S. The task is to print all unique permutations of the given string that may contain dulplicates in lexicographically sorted order. 
"""

class Solution:
    def find_permutation(self, S):
        m = [0 for _ in range(len(S))]
        ans = []
        
        def fun(st, sa, ans, m):
            if len(sa) == len(st):
                if sa not in ans:
                    ans.append(sa)
                
            for i in range(len(st)):
                if m[i] == 0:
                    sa += st[i]
                    m[i] = 1
                    fun(st, sa, ans, m)
                    m[i] = 0
                    sa = sa[:len(sa) - 1]
        
        fun(S, "", ans, m)
        return(ans)

if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        S=input()
        ob = Solution()
        ans = ob.find_permutation(S)
        ans.sort()
        for i in ans:
            print(i,end=" ")
        print()
