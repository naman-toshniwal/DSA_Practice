"""
You are given N elements and your task is to Implement a Stack in which you can get a minimum element in O(1) time.
"""

class stack:
    def __init__(self):
        self.s=[]
        self.minEle=None
        self.minstack=[]

    def push(self,x):
        if not self.s:
            self.s.append(x)
            self.minstack.append(x)
        else:
            self.s.append(x)
            self.minstack.append(min(x,self.minstack[-1]))

    def pop(self):
        if not self.s:
            return -1
        else:
            self.minstack.pop()
            return self.s.pop()
        
    def getMin(self):
        if not self.s:
            return -1
        return self.minstack[-1]

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        q = int(input())
        arr = [int(x) for x in input().split()]
        stk=stack()  
        qi = 0
        qn=1

        while qn <= q:
            qt = arr[qi]
            if qt == 1:
                stk.push(arr[qi+1])
                qi+=2
            elif qt==2:
                print(stk.pop(),end=' ')
                qi+=1
            else:
                print(stk.getMin(),end=' ')
                qi+=1
            qn+=1
        print()
