"""
Suppose there is a circle. There are N petrol pumps on that circle. You will be given two sets of data.
1. The amount of petrol that every petrol pump has.
2. Distance from that petrol pump to the next petrol pump.
Find a starting point where the truck can start to get through the complete circle without exhausting its petrol in between.
Note :  Assume for 1 litre petrol, the truck can go 1 unit of distance.
"""

'''
    lis[][0]:Petrol
    lis[][1]:Distance
'''

class Solution:
    def tour(self,lis, n):
        capacity, deficit, start = 0, 0, 0
        
        for i in range(n):
            capacity += lis[i][0] - lis[i][1]
            
            if capacity < 0:
                start = i+1
                deficit += capacity
                capacity = 0
        
        if deficit + capacity > 0:
            return start
        return -1

if __name__ == '__main__': 
    t = int(input())
    for i in range(t):
        n = int(input())
        arr=list(map(int, input().strip().split()))
        lis=[]
        for i in range(1, 2*n, 2):
            lis.append([ arr[i-1], arr[i] ])
        print(Solution().tour(lis, n))
