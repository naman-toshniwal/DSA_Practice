"""
Given an integer N and an integer D, rotate the binary representation of the integer N by D digits to the left as well as right and return the results in their decimal representation after each of the rotation.
Note: Integer N is stored using 16 bits. i.e. 12 will be stored as 0000000000001100.
"""

class Solution:
    def rotate(self, n, d):
        d=d%16
        x,y=(n>>(16-d)),n&((1<<d)-1)
        return [((n-(x<<(16-d)))<<d)+x,((y<<(16-d))+(n>>d))]

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, d = input().strip().split(" ")
        n, d = int(n), int(d)
        ob = Solution()
        ans = ob.rotate(n, d)
        print(ans[0])
        print(ans[1])
