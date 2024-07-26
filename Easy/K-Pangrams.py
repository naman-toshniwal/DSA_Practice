"""
Given a string str and an integer k, return true if the string can be changed into a pangram after at most k operations, else return false.

A single operation consists of swapping an existing alphabetic character with any other alphabetic character.

Note - A pangram is a sentence containing every letter in the english alphabet.
"""

from collections import Counter

class Solution:
    def kPangram(self,string, k):
        string = string.replace(' ', '')
        mp = Counter(string)
        cnt, total = len(mp.keys()), sum(mp.values())
        return k + cnt >= 26 and total >= 26

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        string = input()
        K = int(input())
        ob = Solution()
        a = ob.kPangram(string, K)
        if a:
            print("true")
        else:
            print("false")
