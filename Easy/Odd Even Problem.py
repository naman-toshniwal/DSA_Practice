"""
Given a string s of lowercase English characters, find out whether the summation of x and y is even or odd, where x is the count of distinct characters that occupy even positions in English alphabets and have even frequency, y is the count of distinct characters which occupy odd positions in English alphabets and have odd frequency.
Note: Positive means greater than zero.
"""

class Solution:
    def oddEven(self, s : str) -> str:
        ans = 0
        d = {}
        
        for i in s:
            if i not in d:
                d.update({i:1})
            else:
                d[i]+=1
                
        for i in d:
            if d[i]%2==1 and (ord(i))%2==1:
                ans+=1
            elif d[i]%2==0 and (ord(i))%2==0:
                ans+=1
                
        return 'EVEN' if ans%2==0 else 'ODD'

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = (input())
        obj = Solution()
        res = obj.oddEven(s)
        print(res)
