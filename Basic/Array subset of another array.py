"""
Given two arrays: a1[0..n-1] of size n and a2[0..m-1] of size m, where both arrays may contain duplicate elements. The task is to determine whether array a2 is a subset of array a1. It's important to note that both arrays can be sorted or unsorted. Additionally, each occurrence of a duplicate element within an array is considered as a separate element of the set.
"""

def isSubset( a1, a2, n, m):
        n = len(a1)
        m = len(a2)
        
        for i in range(0,m):
            if a2[i] in a1:
                a1.remove(a2[i])
            else:
                return "No"
        
        return "Yes"

def main():
    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]
        print(isSubset( a1, a2, n, m))
        T -= 1


if __name__ == "__main__":
    main()
