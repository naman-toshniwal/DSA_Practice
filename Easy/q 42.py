"""
Implement a Queue using 2 stacks s1 and s2 .
A Query Q is of 2 Types
(i) 1 x (a query of this type means  pushing 'x' into the queue)
(ii) 2   (a query of this type means to pop element from queue and print the poped element)

Note :- If there is no element return -1 as answer while popping.
"""

def Push(x,stack1,stack2):
    stack1.append(x)
    stack2.append(x)

def Pop(stack1,stack2):
    if stack1 == []:
        return -1
    else:
        return stack1.pop(0)
    
    if stack2 == []:
        return -1
    else:
        return stack2.pop(0)
    
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        qry=int(input())
        qtyp_qry=list(map(int, input().strip().split()))
        
        i=0
        stack1=[]
        stack2=[]
        while i <len(qtyp_qry):
            if qtyp_qry[i]==1:
                Push(qtyp_qry[i+1],stack1,stack2)
                i+=2
            else:
                print(Pop(stack1,stack2),end=' ')
                i+=1
                
        print()
