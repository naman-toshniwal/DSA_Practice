"""
Given a number n, find the number of binary strings of length n that contain consecutive 1's in them. Since the number can be very large, return the answer after modulo with 1e9+7.
"""

#User function Template for python3
class Solution:
    def numberOfConsecutiveOnes (ob, n):
        zero_invalid, one_invalid = 1, 1
        M = 10**9+7
        
        for _ in range(1, n):
            zero_invalid, one_invalid = (zero_invalid+one_invalid)%M, zero_invalid
        return (pow(2, n)%M + M - (zero_invalid+one_invalid))%M

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        print(ob.numberOfConsecutiveOnes(N))
