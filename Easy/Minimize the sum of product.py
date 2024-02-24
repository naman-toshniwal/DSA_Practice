"""
You are given two arrays, A and B, of equal size N. The task is to find the minimum value of A[0] * B[0] + A[1] * B[1] + .... + A[N-1] * B[N-1], where shuffling of elements of arrays A and B is allowed.
"""

class Solution:
    def minValue(self, a, b, n):
        a.sort()
        a.reverse()
        b.sort()
        
        dot_product = sum(i*j for i, j in zip(a, b))
        return dot_product

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob=Solution()
        print(ob.minValue(a, b, n))

        T -= 1

if __name__ == "__main__":
    main()
