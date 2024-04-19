"""
Find the largest rectangular area possible in a given histogram where the largest rectangle can be made of a number of contiguous bars. For simplicity, assume that all bars have the same width and the width is 1 unit, there will be N bars height of each bar will be given by the array arr.
"""

class Solution:
    def getMaxArea(self,histogram):
        maxarea=0
        stack=[]
        
        for i in range(n+1):
            while stack and (i==n or histogram[stack[-1]]>histogram[i]):
                height=histogram[stack.pop()]
                
                if not stack:
                    width=i
                else:
                    width=abs(i-stack[-1]-1)
                maxarea=max(maxarea,width*height)
            stack.append(i)
        return maxarea

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.getMaxArea(a))
