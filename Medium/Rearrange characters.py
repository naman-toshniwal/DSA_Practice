"""
Given a string S with repeated characters. The task is to rearrange characters in a string such that no two adjacent characters are the same.
Note: The string has only lowercase English alphabets and it can have multiple solutions. Return any one of them.
"""

class Solution :
    def rearrangeString(self, str1):
        myDict = {}
        
        for i in str1:
            if i in myDict.keys():
                myDict[i] += 1
            else:
                myDict[i] = 1
        
        myDict = sorted(myDict.items(), key=lambda x: x[1], reverse = True)
        i = 0
        
        if len(str1)%2 == 0:
            half = len(str1)//2
        else:
            half = len(str1)//2+1
        
        for k, v in myDict:
            if v > half:
                return '-1'
            
            while(v):
                str1 = str1[:i]+k+str1[i+1:]
                v -= 1
                i+=2
                if(i>=len(str1)):
                    i = 1
                    
        return str1

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        str1 = input()
        solObj = Solution()
        str2 = solObj.rearrangeString(str1)
        if str2=='-1':
            print(0)
        elif sorted(str1)!=sorted(str2):
            print(0)
        else:
            for i in range(len(str2)-1):
                if str2[i]==str2[i+1]:
                    print(0)
                    break
            else:
                print(1)
