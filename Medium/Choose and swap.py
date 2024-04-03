"""
You are given a string s of lower case english alphabets. You can choose any two characters in the string and replace all the occurences of the first character with the second character and replace all the occurences of the second character with the first character. Your aim is to find the lexicographically smallest string that can be obtained by doing this operation at most once.
"""

class Solution:
    def chooseandswap (self, A):
        char_set = list(set(A))
        i=0  
        char_set.sort()
        
        while char_set:
            if char_set[0] < A[i]:
                return A.replace(A[i], '*').replace(char_set[0], A[i]).replace('*', char_set[0])
            
            if char_set[0] == A[i]:    
                char_set.pop(0)
            i+=1
        return A

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        A = input()
        ans = ob.chooseandswap(A)
        print(ans)
