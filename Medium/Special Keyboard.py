"""
Imagine you have a special keyboard with the following keys: 

Key 1:  Prints 'A' on screen
Key 2: (Ctrl-A): Select screen
Key 3: (Ctrl-C): Copy selection to buffer
Key 4: (Ctrl-V): Print buffer on screen appending it after what has already been printed.

Find maximum numbers of A's that can be produced by pressing keys on the special keyboard N times. 
"""

class Solution:
    def optimalKeys(self, N):
        arr = [0] * (N + 1)
        
        if N < 7:
            return N
        
        for i in range(7):
            arr[i] = i
        
        for i in range(7, N + 1):
            arr[i] = max(3 * arr[i - 5 + 1], 4 * arr[i - 6 + 1])
        return arr[N]

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        print(ob.optimalKeys(N))
