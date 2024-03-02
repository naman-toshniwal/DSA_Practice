"""
The cost of stock on each day is given in an array A[] of size N. Find all the segments of days on which you buy and sell the stock such that the sum of difference between sell and buy prices is maximized. Each segment consists of indexes of two elements, first is index of day on which you buy stock and second is index of day on which you sell stock.
Note: Since there can be multiple solutions, the driver code will print 1 if your answer is correct, otherwise, it will return 0. In case there's no profit the driver code will print the string "No Profit" for a correct solution.
"""

class Solution:
    def stockBuySell(self, A, n):
        result = []
        
        for i in range(1, n):
            if A[i] >= A[i - 1]:
                result.append((i-1, i))
        
        return result

def check(ans,A,p):
    c = 0
    for i in range(len(ans)):
        c += A[ans[i][1]]-A[ans[i][0]]
    if(c==p):
        return 1 
    else:
        return 0

if __name__=='__main__':
    t = int(input())
    while(t>0):
        n = int(input())
        A = [int(x) for x in input().strip().split()]
        ob = Solution()
        ans = ob.stockBuySell(A,n)
        p=0
        for i in range(n-1):
            p += max(0,A[i+1]-A[i])
        if(len(ans) == 0):
            print("No Profit",end="")
        else:
            print(check(ans,A,p),end="")
        print()
        t-=1
