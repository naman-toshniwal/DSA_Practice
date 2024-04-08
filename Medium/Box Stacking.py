"""
You are given a set of N types of rectangular 3-D boxes, where the ith box has height h, width w and length l. Your task is to create a stack of boxes which is as tall as possible, but you can only stack a box on top of another box if the dimensions of the 2-D base of the lower box are each strictly larger than those of the 2-D base of the higher box. Of course, you can rotate a box so that any side functions as its base.It is also allowable to use multiple instances of the same type of box. Your task is to complete the function maxHeight which returns the height of the highest possible stack so formed.
 
Note: Base of the lower box should be strictly larger than that of the new box we're going to place. This is in terms of both length and width, not just in terms of area. So, two boxes with same base cannot be placed one over the other.
"""

class Solution:
    def maxHeight(self,height, width, length, n):
        boxes = []
        
        for i in range(n):
            a = height[i]
            b = width[i]
            c = length[i]
            boxes.append([a,b,c])
            boxes.append([b,c,a])
            boxes.append([c,a,b])
            boxes.append([b,a,c])
            boxes.append([c,b,a])
            boxes.append([a,c,b])
    
        boxes.sort(key=lambda x: x[0] * x[1], reverse=True)
        dp = [x[2] for x in boxes]

        for i in range(1, len(boxes)):
            for j in range(i):
                if boxes[i][0] < boxes[j][0] and boxes[i][1] < boxes[j][1]:
                    test = dp[j] + boxes[i][2]
                    dp[i] = max(dp[i], test)
                    
        return max(dp)

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        height = list(map(int, input().strip().split()))
        width = list(map(int, input().strip().split()))
        length = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.maxHeight(height, width, length, n))
