"""
Given two lists V1 and V2 of sizes n and m respectively. Return the list of elements common to both the lists and return the list in sorted order. Duplicates may be there in the output list.
"""

#User function Template for python3

class Solution:
    def common_element(self,v1,v2):
        count = {}
        ans = []
        
        for i in v1:
            count[i] = count.get(i, 0) + 1
            
        for i in v2:
            if i in count and count[i] > 0:
                count[i] = count[i] - 1
                ans.append(i)
        
        ans.sort()
        return ans

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n=int(input())
        v1=list(map(int,input().split()))
        m=int(input())
        v2=list(map(int,input().split()))
        ob=Solution()
        ans=ob.common_element(v1, v2);
        for i in ans:
            print(i,end = " ")
        print()
