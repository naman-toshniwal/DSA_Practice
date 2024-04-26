"""
Given a number N and a value K. From the right, set the Kth bit in the binary representation of N. The position of Least Significant Bit(or last bit) is 0, the second last bit is 1 and so on. 
"""

class Solution:
    def setKthBit(self, N, K):
        return (N|1<<K);

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N,K = input().split()
        N = int(N)
        K = int(K)
        ob = Solution()
        ans = ob.setKthBit(N,K)
        print(ans)
