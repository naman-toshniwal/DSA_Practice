"""
You are given an array arr. Your task is to find the longest length of a good sequence. A good sequence {x1, x2, .. xn} is an alternating sequence if its elements satisfy one of the following relations :

1.  x1 < x2 > x3 < x4 > x5. . . . . and so on
2.  x1 >x2 < x3 > x4 < x5. . . . . and so on
"""

class Solution:
    def alternatingMaxLength(self, arr):
        incre=1
        decre=1
        
        for i in range(1,len(arr)):
            if arr[i]>arr[i-1]:
                incre=decre+1
            elif arr[i]<arr[i-1]:
                decre=incre+1
                
        return max(incre,decre)

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    tc = int(data[0])
    for i in range(1, tc + 1):
        s = data[i].strip().split()
        nums = list(map(int, s))
        obj = Solution()
        ans = obj.alternatingMaxLength(nums)
        print(ans)
