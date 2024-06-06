"""
Given an integer array(0-based indexing) a of size n. Your task is to return the maximum value of the sum of i*a[i] for all 0<= i <=n-1, where a[i] is the element at index i in the array. The only operation allowed is to rotate(clockwise or counterclockwise) the array any number of times.
"""

def max_sum(a,n):
    summ = sum(a)
    sum_pos = 0
    j = n-1
    last = a[j]
    
    for i in range(n):
        sum_pos += (a[i]*i)
    ans = sum_pos    
    
    for i in range(1, n):
        sum_pos = sum_pos + summ - (last*n)
        ans = max(sum_pos, ans)
        j -= 1
        last = a[j]
    return ans  

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(max_sum(arr, n))
