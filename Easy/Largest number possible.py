"""
Given two numbers 'N' and 'S' , find the largest number that can be formed with 'N' digits and whose sum of digits should be equals to 'S'. Return -1 if it is not possible.
"""

class Solution:
    def findLargest(self, N, S):
        if (S == 0 and  N > 1):
            return -1
        answer = ""
        
        for i in range(N):
            if S >= 9:
                answer += "9"
                S -= 9
            else:
                answer += str(S)
                S -= S
        
        if (S > 0):
            return -1
        else:
            return int(answer)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, S = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.findLargest(N, S))