"""
In a restaurant, two waiters, A and B, receive n orders per day, earning tips as per arrays arr[i] and brr[i] respectively. If A takes the ith order, the tip is arr[i] rupees; if B takes it, the tip is brr[i] rupees.

To maximize total tips, they must distribute the orders such that:

A can handle at most x orders
B can handle at most y orders
Given that x + y ≥ n, all orders can be managed by either A or B. Return the maximum possible total tip after processing all the orders.
"""

from typing import List

class Solution:
    def maxTip(self, n : int, x : int, y : int, arr : List[int], brr : List[int]) -> int:
        tp = zip(arr, brr)
        sorted_tips = sorted(tp, key=lambda t: abs(t[0] - t[1]), reverse=True)
        cntA, cntB, total = 0, 0, 0
        
        for a, b in sorted_tips:
            if (a >= b and cntA < x) or cntB == y:
                total += a
                cntA += 1
            else:
                total += b
                cntB += 1
                
        return total

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
        n = int(input())
        x = int(input())
        y = int(input())
        arr = IntArray().Input(n)
        brr = IntArray().Input(n)
        obj = Solution()
        res = obj.maxTip(n, x, y, arr, brr)
        print(res)
