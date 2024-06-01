"""
Given a number n, Your task is to swap the two nibbles and find the resulting number. 

A nibble is a four-bit aggregation, or half an octet. There are two nibbles in a byte. For example, the decimal number 150 is represented as 10010110 in an 8-bit byte. This byte can be divided into two nibbles: 1001 and 0110.
"""

class Solution:
    def swapNibbles (self, num: int) -> int:
        for _ in range(4):
            lastBit = num & 1
            num >>= 1
            num |= (lastBit << (8-1))
        return num

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.swapNibbles(n))
