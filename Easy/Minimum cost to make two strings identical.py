"""
Given two strings x and y, and two values costX and costY, the task is to find the minimum cost required to make the given two strings identical. You can delete characters from both the strings. The cost of deleting a character from string X is costX and from Y is costY. The cost of removing all characters from a string is the same.
"""

class Solution:
    def findMinCost(self, x, y, costX, costY):
        m,n=len(x),len(y)
        prv=[0 for _ in range(m+1)]
        cur=[0 for _ in range(m+1)]
        
        for b in range(1,n+1):
            for a in range(1,m+1):
                if x[a-1]==y[b-1]:
                    cur[a]=prv[a-1]+1
                cur[a]=max(cur[a],prv[a],cur[a-1])
            prv=cur[:]
        mx=cur[-1]
        return (m-mx)*costX+(n-mx)*costY

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        X, Y, costX, costY = input().split()
        costX = int(costX)
        costY = int(costY)
        ob = Solution()
        ans = ob.findMinCost(X, Y, costX, costY)
        print(ans)
