"""
You are given a number n, Return the count of total numbers from 1 to n containing 4 as a digit.
"""

class Solution:
    def countNumberswith4(self, n : int) -> int:
        count = 0
        
        for i in range(n+1):
            if '4' in str(i):
                count += 1
        
        return count

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        obj = Solution()
        res = obj.countNumberswith4(n)
        print(res)
