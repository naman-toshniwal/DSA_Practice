"""
Rohan has a special love for the matrices especially for the first element of the matrix. Being good at Mathematics, he also loves to solve the different problem on the matrices. So one day he started to multiply the matrix with the original matrix.  The elements of the original matrix a are given by [a00=1 , a01=1, a10=1, a11=0].
Given the power of the matrix, n calculate the an and return the a10 element mod 1000000007.
"""

class Solution:
    def firstElement (self, n):
        first_element = 1
        second_element = 1
        res = 0
        
        if n <= 2:
            return first_element
        
        for i in range(3,n+1):
            res = (first_element+second_element)%1000000007
            first_element = second_element
            second_element = res
        return res

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        ob = Solution()
        print(ob.firstElement(n))
