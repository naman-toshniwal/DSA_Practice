"""
Given an input stream A of n characters consisting only of lower case alphabets. While reading characters from the stream, you have to tell which character has appeared only once in the stream upto that point. If there are many characters that have appeared only once, you have to tell which one of them was the first one to appear. If there is no such character then append '#' to the answer.

NOTE:
1. You need to find the answer for every i (0 <= i < n)
2. In order to find the solution for every i you need to consider the string from starting position till ith position.
"""

class Solution:
    def FirstNonRepeating(self, A):
        di={}
        q=[]
        ans=""
        
        for i in A:
            if i not in di.keys():
                di[i]=1
            else:
                di[i]+=1
            q.append(i)
            
            while(len(q)):
                if(di[q[0]]>1):
                    q.pop(0)
                else:
                    ans+=q[0]
                    break
                
            if not len(q):
                ans+='#'
        return ans

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        A = input()
        ob = Solution()
        ans = ob.FirstNonRepeating(A)
        print(ans)
