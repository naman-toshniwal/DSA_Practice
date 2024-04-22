"""
Given an array of strings arr[] of size N, find if there exists 2 strings arr[i] and arr[j] such that arr[i]+arr[j] is a palindrome i.e the concatenation of string arr[i] and arr[j] results into a palindrome.
"""

class Solution:
    def palindromepair(self, N, arr):
        index = {word:i for i,word in enumerate(arr)}
        
        for i,word in enumerate(arr):
            for j in range(len(word)+1):
                left = word[:j]
                right = word[j:]
                
                if left ==left[::-1] and right[::-1] in index and index[right[::-1]]!=i:
                    return 1
                
                if right==right[::-1] and left[::-1] in index and index[left[::-1]]!=i:
                    return 1
                    
        return 0

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=[]
        for i in range(N):
            s = input()
            arr.append(s)
        
        ob = Solution()
        print(ob.palindromepair(N,arr))
