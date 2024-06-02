"""
Given a list s that initially contains only a single value 0. There will be q queries of the following types:

0 x: Insert x in the list
1 x: For every element a in s, replace it with a ^ x. ('^' denotes the bitwise XOR operator)
Return the sorted list after performing the given q queries.
"""

from typing import List

class Solution:
    def constructList(self, q : int, queries : List[List[int]]) -> List[int]:
        xr,lis=0,[]
        
        while queries:
            a,b=queries.pop();
            
            if a==0:
                lis.append(b^xr)
            else:
                xr^=b
                
        lis.append(xr)        
        return sorted(lis)    

class IntMatrix:
    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()

class IntArray:
    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        q = int(input())
        queries = IntMatrix().Input(q, 2)
        obj = Solution()
        res = obj.constructList(q, queries)
        IntArray().Print(res)
