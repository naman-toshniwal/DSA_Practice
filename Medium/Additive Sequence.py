"""
Given a string n, your task is to find whether it contains an additive sequence or not. A string n contains an additive sequence if its digits can make a sequence of numbers in which every number is addition of previous two numbers. You are required to complete the function which returns true if the string is a valid sequence else returns false. For better understanding check the examples.

Note: A valid string should contain at least three digit to make one additive sequence. 
"""

class Solution:
    def isAdditiveSequence(self, n):
        def is_valid(n1, n2, rem):
            if not rem:
                return True
            sum_n = str(n1 + n2)
            
            if rem.startswith(sum_n):
                return is_valid(n2, int(sum_n), rem[len(sum_n):])
            return False
        length = len(n)    
        
        for i in range(1, length):
            for j in range(i + 1, length):
                n1 = int(n[:i])
                n2 = int(n[i:j])
                
                if is_valid(n1, n2, n[j:]):
                    return 1
        return 0
  
if __name__ == "__main__":
    sol = Solution()
    t = int(input())
    for _ in range(t):
        s = input()
        print(sol.isAdditiveSequence(s))
