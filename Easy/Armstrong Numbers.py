"""
You are given a 3-digit number n, Find whether it is an Armstrong number or not.

An Armstrong number of three digits is a number such that the sum of the cubes of its digits is equal to the number itself. 371 is an Armstrong number since 33 + 73 + 13 = 371. 

Note: Return "true" if it is an Armstrong number else return "false".
"""

class Solution:
    def armstrongNumber(self, n):
        hundreds = n // 100  
        tens = (n % 100) // 10  
        units = n % 10 
        
        if ((hundreds**3 + tens**3 + units**3) == n):
            return "true"
        else:
            return "false"

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = input()
        n = int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))
