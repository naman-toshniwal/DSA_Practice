"""
Write a program to find the sum of the given series 1+2+3+ . . . . . .(N terms) 
"""

class Solution:
    def seriesSum(self, n : int) -> int:
        return (n*(n + 1) // 2)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        obj = Solution()
        res = obj.seriesSum(n)
        print(res)
