"""
The task is to complete the insert() function which is used to implement Insertion Sort.
"""

class Solution:
    def insert(self, alist, index, n):
        j=index-1
        key=alist[index]
        
        while j>=0 and key<alist[j]:
            alist[j+1]=alist[j]
            j-=1
        alist[j+1]=key
           
    def insertionSort(self, alist, n):
        for i in range(1,n):
            self.insert(alist,i,n)

if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().insertionSort(arr,n)
    
        for i in range(n):
            print(arr[i],end=" ")
        print()
