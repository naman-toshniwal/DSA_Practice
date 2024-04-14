"""
Given a sorted dictionary of an alien language having N words and k starting alphabets of standard dictionary. Find the order of characters in the alien language.
Note: Many orders may be possible for a particular test case, thus you may return any valid order and output will be 1 if the order of string returned by the function is correct else 0 denoting incorrect string returned.
"""

from collections import deque

class Solution:
    def findOrder(self,alien_dict, N, K):
        adj=[[] for _ in range(K)]

        for i in range(N-1):
            s1=alien_dict[i]
            s2=alien_dict[i+1]
            length=min(len(s1),len(s2))

            for p in range(length):
                if s1[p]!=s2[p]:
                    adj[ord(s1[p])-ord('a')].append(ord(s2[p])-ord('a'))
                    break
     
        V=K
        indegree=[0]*V
        for i in range(V):
            for j in adj[i]:
                indegree[j]+=1
  
        q=deque()
        for i in range(V):
            if indegree[i]==0:
                q.append(i)

        ans=[]
        while(len(q)):
            node=q.popleft()
            ans.append(chr(ord('a')+node))

            for i in adj[node]:
                indegree[i]-=1
                if indegree[i]==0:
                    q.append(i)

        return ans

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)
