"""
Given an array A of integers and another number K. Find all the unique quadruple from the given array that sums up to K.

Also note that all the quadruples which you return should be internally sorted, ie for any quadruple [q1, q2, q3, q4] the following should follow: q1 <= q2 <= q3 <= q4.
"""

class Solution:
    def fourSum(self, arr, k):
        result = []
        l = len(arr)
        arr = sorted(arr)
        
        for i in range(l-3):
            if i > 0 and arr[i] == arr[i-1]:
                continue
            
            for j in range(i+1, l-2):
                if j > i+1 and arr[j] == arr[j-1]:
                    continue
                a = j + 1
                b = l - 1
                
                while a < b:
                    c = arr[a] + arr[b] + arr[i] + arr[j]
                    if c > k:
                        b -= 1
                    elif c < k:
                        a += 1
                    else:
                        result.append([arr[i], arr[j], arr[a], arr[b]])
                        
                        while a < b and arr[a] == arr[a+1]:
                            a += 1
                        while a < b and arr[b] == arr[b-1]:
                            b -= 1
                        a += 1
                        b -= 1
        
        return result
 
if __name__=='__main__':
    t = int(input())
    while t:
        t-=1
        n, k=map(int,input().split())
        # print(n, k)
        a=list(map(int,input().strip().split()))[:n]
        # print(a)
        ob=Solution()
        ans=ob.fourSum(a, k)
        # print(ans)
        for v in ans:
            for u in v:
                print(u, end=" ")
            print("$", end="")
        if(len(ans)==0):
            print(-1, end="")
        print()
