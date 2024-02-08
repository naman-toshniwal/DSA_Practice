"""
Given an expression string x. Examine whether the pairs and the orders of {,},(,),[,] are correct in exp.
For example, the function should return 'true' for exp = [()]{}{[()()]()} and 'false' for exp = [(]).

Note: The drive code prints "balanced" if function return true, otherwise it prints "not balanced".
"""

class Solution:
    def ispar(self,x):
        stack = []
        brac = {')': '(', ']': '[', '}': '{'}
        
        for i in x:
            if i in ('(', '{', '['):
                stack.append(i)
            else:
                if not stack:
                    return False
                elif stack[-1] != brac[i]:
                    return False
                else:
                    stack.pop()
            
        if stack:
            return False
        else:
            return True

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        s = str(input())
        obj = Solution()
        if obj.ispar(s):
            print("balanced")
        else:
            print("not balanced")